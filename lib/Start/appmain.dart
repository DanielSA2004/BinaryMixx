import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:math';

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
  final TextEditingController _controllerT = TextEditingController();
  final TextEditingController _controllerAI = TextEditingController();
  final TextEditingController _controllerBI = TextEditingController();
  final TextEditingController _controllerCI = TextEditingController();
  final TextEditingController _controllerTI = TextEditingController();

  double? resultado; // Variable para almacenar el resultado del cálculo

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: Align(
        alignment: Alignment.centerLeft,
        child: Column(
          children: [SizedBox(height: 50),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Wrap(
                children: [Column(children: [SizedBox(width: 250, child: TextField(
                controller: _controllerA, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'ANTOINE CONSTANT A',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ), 
              SizedBox(height: 15),
              SizedBox(width: 250, child: TextField(
                controller: _controllerB, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'ANTOINE CONSTANT B',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ),
              SizedBox(height: 15),
              SizedBox(width: 250, child: TextField(
                controller: _controllerC, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'ANTOINE CONSTANT C',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ), 
              SizedBox(height: 15),
              SizedBox(width: 250, child: TextField(
                controller: _controllerT, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'SATURATION TEMPERATURE',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              )
              ],
              ),
              SizedBox(width: 15),
              Column(children: [SizedBox(width: 250, child: TextField(
                controller: _controllerAI, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'CONSTANT A II',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ), 
              SizedBox(height: 15),
              SizedBox(width: 250, child: TextField(
                controller: _controllerBI, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'CONSTANT B II',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ),
              SizedBox(height: 15),
              SizedBox(width: 250, child: TextField(
                controller: _controllerCI, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'CONSTANT C II',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ), 
              SizedBox(height: 15),
              SizedBox(width: 250, child: TextField(
                controller: _controllerTI, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
                  labelStyle: GoogleFonts.orbitron(),
                  labelText: 'SATURATION TEMPERATURE II',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              )
              ],)
              ],
              ),
            ),
            SizedBox(height: 15),
            ElevatedButton(
              onPressed: () {
                // Convierte el texto a número (si es válido)
                double? valorA = double.tryParse(_controllerA.text);
                double? valorB = double.tryParse(_controllerB.text);
                double? valorC = double.tryParse(_controllerA.text);
                double? valorT = double.tryParse(_controllerT.text);
                double? valorAI = double.tryParse(_controllerAI.text);
                double? valorBI = double.tryParse(_controllerBI.text);
                double? valorCI = double.tryParse(_controllerAI.text);
                double? valorTI = double.tryParse(_controllerTI.text);

                if (valorA != null && valorB !=null && valorC != null && valorT != null && valorAI != null && valorBI !=null && valorCI != null && valorTI != null){
                  setState(() {

                  // ignore: unused_local_variable, non_constant_identifier_names
                  double PsatI = exp(valorA - (valorB/(valorT+valorC)));
                  // ignore: unused_local_variable, non_constant_identifier_names
                  double PsatII = exp(valorAI - (valorBI/(valorTI+valorCI)));
                  
                  },);
                }
                
                

                },
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                padding: EdgeInsets.symmetric(vertical: 15, horizontal: 30)
              ),  
              child: Text("Calcular", style: GoogleFonts.orbitron()),
            ),
            if (resultado != null)
              Text(
                "Resultado: $resultado",
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: Colors.white)),
              ),
          ],
        ),
      ),
      backgroundColor: Color.fromARGB(255, 11, 9, 31),
    );
  }
}
