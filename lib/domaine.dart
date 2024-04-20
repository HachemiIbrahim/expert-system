// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'dart:convert';

class Symptomp {
  final String description;
  Symptomp({
    required this.description,
  });

  Symptomp copyWith({
    String? description,
  }) {
    return Symptomp(
      description: description ?? this.description,
    );
  }

  Map<String, dynamic> toMap() {
    return <String, dynamic>{
      'description': description,
    };
  }

  factory Symptomp.fromMap(Map<String, dynamic> map) {
    return Symptomp(
      description: map['description'] as String,
    );
  }

  String toJson() => json.encode(toMap());

  factory Symptomp.fromJson(String source) =>
      Symptomp.fromMap(json.decode(source) as Map<String, dynamic>);

  @override
  String toString() => 'Symptomp(description: $description)';

  @override
  bool operator ==(covariant Symptomp other) {
    if (identical(this, other)) return true;

    return other.description == description;
  }

  @override
  int get hashCode => description.hashCode;
}

class Problem {
  final String title;
  final String description;
  final String solution;
  Problem({
    required this.title,
    required this.description,
    required this.solution,
  });

  Map<String, dynamic> toMap() {
    return <String, dynamic>{
      'title': title,
      'description': description,
      'solution': solution,
    };
  }

  factory Problem.fromMap(Map<String, dynamic> map) {
    return Problem(
      title: map['title'] as String,
      description: map['description'] as String,
      solution: map['solution'] as String,
    );
  }

  String toJson() => json.encode(toMap());

  factory Problem.fromJson(String source) =>
      Problem.fromMap(json.decode(source) as Map<String, dynamic>);

  Problem copyWith({
    String? title,
    String? description,
    String? solution,
  }) {
    return Problem(
      title: title ?? this.title,
      description: description ?? this.description,
      solution: solution ?? this.solution,
    );
  }

  @override
  String toString() =>
      'Problem(title: $title, description: $description, solution: $solution)';

  @override
  bool operator ==(covariant Problem other) {
    if (identical(this, other)) return true;

    return other.title == title &&
        other.description == description &&
        other.solution == solution;
  }

  @override
  int get hashCode => title.hashCode ^ description.hashCode ^ solution.hashCode;
}
