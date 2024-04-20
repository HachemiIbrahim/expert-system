import 'package:ai_project/domaine.dart';
import 'package:ai_project/repo.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

class FirstScreen extends HookConsumerWidget {
  const FirstScreen({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final selectedSymptomp = useState<List<Symptomp>>([]);
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          final selected = selectedSymptomp.value;
          if (selected.isNotEmpty && selected.length == 3) {
            Navigator.of(context).pushNamed('/second', arguments: selected);
          }
        },
        child: const Icon(Icons.arrow_forward),
      ),
      body: Column(
        children: [
          const SizedBox(
            height: 50,
          ),
          const Text(
            'Select your problems',
            style: TextStyle(fontSize: 30),
          ),
          Expanded(
            child: ref.watch(symptompsProvider).when(
                data: (symptomps) {
                  return ListView.builder(
                      itemCount: symptomps.length,
                      itemBuilder: (context, index) {
                        final symptomp = symptomps[index];
                        return ListTile(
                          title: Text(symptomp.description),
                          trailing: Checkbox(
                            value: selectedSymptomp.value.contains(symptomp),
                            onChanged: (value) {
                              if (value!) {
                                if (selectedSymptomp.value.length >= 3) {
                                  return;
                                }
                                selectedSymptomp.value = [
                                  ...selectedSymptomp.value,
                                  symptomp
                                ];
                              } else {
                                selectedSymptomp.value = selectedSymptomp.value
                                    .where((s) => s != symptomp)
                                    .toList();
                              }
                            },
                          ),
                        );
                      });
                },
                error: (e, tr) {
                  return Center(child: Text('Error: $e'));
                },
                loading: () => const Center(
                      child: CircularProgressIndicator(),
                    )),
          ),
        ],
      ),
    );
  }
}
