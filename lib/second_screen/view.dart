import 'package:ai_project/domaine.dart';
import 'package:ai_project/repo.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class SecondScreen extends ConsumerWidget {
  const SecondScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final arguments =
        ModalRoute.of(context)!.settings.arguments as List<Symptomp>;
    return Scaffold(
        body: ref.watch(problemProvider(arguments)).when(
              data: (problem) {
                return Column(
                  children: [
                    const SizedBox(
                      height: 50,
                    ),
                    Text(
                      problem.title,
                      style: const TextStyle(fontSize: 30),
                    ),
                    Text(
                      problem.description,
                      style: const TextStyle(fontSize: 20),
                    ),
                    Text(
                      problem.solution,
                      style: const TextStyle(fontSize: 20),
                    ),
                  ],
                );
              },
              loading: () => const Center(
                child: CircularProgressIndicator(),
              ),
              error: (error, stack) => Center(
                child: Text('Error: $error'),
              ),
            ));
  }
}
