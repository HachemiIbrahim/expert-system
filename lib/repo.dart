import 'dart:convert';

import 'package:ai_project/domaine.dart';
import 'package:dio/dio.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;

final dioProvider = Provider<Dio>((ref) => Dio());

final repositoryProvider = Provider<Repository>((ref) {
  return Repository();
});

final symptompsProvider = FutureProvider<List<Symptomp>>((ref) {
  final repository = ref.watch(repositoryProvider);
  return repository.getSymptomps();
});

final problemProvider = FutureProvider.family
    .autoDispose<Problem, List<Symptomp>>((ref, symptomps) {
  final repository = ref.watch(repositoryProvider);
  return repository.getProblem(symptomps);
});

class Repository {
  Future<List<Symptomp>> getSymptomps() async {
    final response =
        await http.get(Uri.parse("http://192.168.52.150:8000/symptoms"));

    final list = jsonDecode(response.body);
    final List<Symptomp> symptomps = [];
    for (var item in list) {
      symptomps.add(Symptomp.fromMap(item));
    }
    return symptomps;
  }

  Future<Problem> getProblem(List<Symptomp> symptomp) async {
    final data = getSymptompMap(symptomp);
    final response = await http.post(
        Uri.parse("http://192.168.52.150:8000/diagnose"),
        body: jsonEncode(data),
        headers: {'Content-Type': 'application/json'});
    if (response.statusCode == 200) {
      final problem = jsonDecode(response.body);

      return Problem.fromMap(problem);
    }

    throw Exception('There is no problem');
  }

  // create function that get list and return map in format
  // {symptop1: description, symptop2: description, symptop3: description}
  // and return the map

  Map<String, String> getSymptompMap(List<Symptomp> symptomp) {
    Map<String, String> symptompMap = {};
    symptompMap['symptom1'] = symptomp[0].description;
    symptompMap['symptom2'] = symptomp[1].description;
    symptompMap['symptom3'] = symptomp[2].description;
    return symptompMap;
  }
}
