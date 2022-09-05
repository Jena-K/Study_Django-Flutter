// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:fluutermobile/screens/home.dart';

void main() {
  runApp(PlanApp());
}

class PlanApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '일정관리',
      home: HomeScreen(),
    );
  }
}
