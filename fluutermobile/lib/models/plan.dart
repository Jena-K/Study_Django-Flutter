class Solution {
  int id;
  String solution;

  Solution({required this.id, required this.solution});

  factory Solution.fromJason(Map<String, dynamic> json) {
    return Solution(
      id: json['id'],
      solution: json['solution'],
    );
  }
}
