import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:math';
import 'package:fl_chart/fl_chart.dart';

class MymainApp extends StatefulWidget {
  const MymainApp({super.key, required this.title});

  final String title;

  @override
  State<MymainApp> createState() => _MymainAppState();
}

class _MymainAppState extends State<MymainApp> {
  final TextEditingController _controllerA = TextEditingController();
  final TextEditingController _controllerB = TextEditingController();
  final TextEditingController _controllerC = TextEditingController();

  final TextEditingController _controllerAI = TextEditingController();
  final TextEditingController _controllerBI = TextEditingController();
  final TextEditingController _controllerCI = TextEditingController();
  final TextEditingController _controllerTI = TextEditingController();

  // Variables para almacenar datos de la gráfica
  List<double> x_1 = [];
  List<double> P = [];
  List<double> y_1 = [];

  // Función para convertir vectores en puntos FlSpot
  List<FlSpot> _createFlSpots(List<double> xValues, List<double> yValues) {
    List<FlSpot> spots = [];
    for (int i = 0; i < xValues.length; i++) {
      spots.add(FlSpot(xValues[i], yValues[i]));
    }
    return spots;
  }

  double? resultado; // Variable para almacenar el resultado del cálculo

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: Wrap(
        children: [
          Align(
              alignment: Alignment.centerLeft,
              child: Column(children: [
                SizedBox(height: 60),
                Text(
                  'DATA INPUT',
                  style: GoogleFonts.orbitron(color: Colors.white),
                ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: const Color.fromARGB(
                            255, 255, 255, 255), // Color del borde
                        width: 1, // Ancho del borde
                      ),
                      borderRadius:
                          BorderRadius.circular(16), // Esquinas redondeadas
                    ),
                    padding: EdgeInsets.all(8.0), // Espaciado interno
                    child: Wrap(
                      children: [
                        Column(
                          children: [
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerA,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'ANTOINE CONSTANT A',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                            SizedBox(height: 15),
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerB,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'ANTOINE CONSTANT B',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                            SizedBox(height: 15),
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerC,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'ANTOINE CONSTANT C',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                            SizedBox(height: 15),
                          ],
                        ),
                        SizedBox(width: 15),
                        Column(
                          children: [
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerAI,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'CONSTANT A II',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                            SizedBox(height: 15),
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerBI,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'CONSTANT B II',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                            SizedBox(height: 15),
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerCI,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'CONSTANT C II',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                            SizedBox(height: 15),
                            SizedBox(
                              width: 250,
                              child: TextField(
                                controller: _controllerTI,
                                style: GoogleFonts.orbitron(
                                    textStyle: TextStyle(
                                        color: const Color.fromARGB(
                                            255, 251, 251, 251))),
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelStyle: GoogleFonts.orbitron(),
                                  labelText: 'SYSTEM TEMPERATURE',
                                  border: OutlineInputBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
                SizedBox(height: 15),
                ElevatedButton(
                  onPressed: () {
                    double? valorA = double.tryParse(_controllerA.text);
                    double? valorB = double.tryParse(_controllerB.text);
                    double? valorC = double.tryParse(_controllerC.text);

                    double? valorAI = double.tryParse(_controllerAI.text);
                    double? valorBI = double.tryParse(_controllerBI.text);
                    double? valorCI = double.tryParse(_controllerCI.text);
                    double? valorTI = double.tryParse(_controllerTI.text);

                    if (valorA != null &&
                        valorB != null &&
                        valorC != null &&
                        valorAI != null &&
                        valorBI != null &&
                        valorCI != null &&
                        valorTI != null) {
                      setState(() {
                        // ignore: non_constant_identifier_names
                        double PsatI =
                            exp(valorA - (valorB / (valorTI + valorC)));
                        // ignore: non_constant_identifier_names
                        double PsatII =
                            exp(valorAI - (valorBI / (valorTI + valorCI)));

                        List<double> x_1 = [
                          0,
                          0.1,
                          0.2,
                          0.3,
                          0.4,
                          0.5,
                          0.6,
                          0.7,
                          0.8,
                          0.9,
                          1
                        ];

                        List<double> x_2 = [
                          1,
                          0.9,
                          0.8,
                          0.7,
                          0.6,
                          0.5,
                          0.4,
                          0.3,
                          0.2,
                          0.1,
                          0
                        ];

                        P.clear();
                        y_1.clear();

                        for (int i = 0; i < x_1.length; i++) {
                          P.add(x_1[i] * PsatI + x_2[i] * PsatII);
                          y_1.add(x_1[i] * PsatI / P[i]);
                        }
                      });
                    }
                  },
                  style: ElevatedButton.styleFrom(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10)),
                      padding:
                          EdgeInsets.symmetric(vertical: 15, horizontal: 30)),
                  child: Text("Calcular", style: GoogleFonts.orbitron()),
                ),
              ])),
          SizedBox(height: 20, width: 20),
          Align(
            alignment: Alignment(1000, 500),
            child: Column(
              children: [
                SizedBox(
                  width: 20,
                  height: 20,
                ),
                SizedBox(
                  height: 300,
                  width: 300,
                  child: LineChart(LineChartData(
                      gridData: FlGridData(show: true),
                      titlesData: FlTitlesData(
                        leftTitles: AxisTitles(
                          sideTitles: SideTitles(
                            showTitles: true,
                            reservedSize: 40,
                            getTitlesWidget: (value, meta) {
                              if (value % 2 == 0) {
                                return Text(
                                  value.toStringAsFixed(0),
                                  style: const TextStyle(
                                      color: Colors.black, fontSize: 12),
                                );
                              }
                              return Container();
                            },
                          ),
                          axisNameWidget: Text(
                            "P (kPa)",
                            style: GoogleFonts.orbitron(
                                fontSize: 14, fontWeight: FontWeight.bold),
                          ),
                          axisNameSize: 30,
                        ),
                        bottomTitles: AxisTitles(
                          sideTitles: SideTitles(
                            showTitles: true,
                            reservedSize: 30,
                            getTitlesWidget: (value, meta) {
                              if (value % 0.2 == 0) {
                                return Text(
                                  value.toStringAsFixed(1),
                                  style: const TextStyle(
                                      color: Colors.black, fontSize: 12),
                                );
                              }
                              return Container();
                            },
                          ),
                          axisNameWidget: Text(
                            "x₁, y₁",
                            style: GoogleFonts.orbitron(
                                fontSize: 14, fontWeight: FontWeight.bold),
                          ),
                          axisNameSize: 30,
                        ),
                        topTitles: const AxisTitles(
                            sideTitles: SideTitles(showTitles: false)),
                        rightTitles: const AxisTitles(
                            sideTitles: SideTitles(showTitles: false)),
                      ),
                      lineBarsData: [
                        LineChartBarData(
                          isCurved: true,
                          color: Colors.blue,
                          spots: _createFlSpots(x_1, P),
                          dotData: FlDotData(show: false),
                        ),
                        LineChartBarData(
                          isCurved: true,
                          color: Colors.orange,
                          spots: _createFlSpots(y_1, P),
                          dotData: FlDotData(show: false),
                        ),
                      ],
                      borderData: FlBorderData(
                        show: true,
                        border: Border.all(
                            color: const Color.fromARGB(255, 242, 205, 92),
                            width: 1),
                      ),
                      backgroundColor: Colors.white)),
                ),
              ],
            ),
          ),
        ],
      ),
      backgroundColor: Color.fromARGB(255, 11, 9, 31),
    );
  }
}
