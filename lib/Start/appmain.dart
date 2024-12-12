import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

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

  double? resultado; // Variable para almacenar el resultado del cálculo

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: Align(
        alignment: Alignment.centerLeft,
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Wrap(
                children: [Column(children: [SizedBox(width: 250, child: TextField(
                controller: _controllerA, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
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
                  labelText: 'ANTOINE CONSTANT B',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              ),
              SizedBox(width: 250, child: TextField(
                controller: _controllerC, // Asocia el TextEditingController
                style: GoogleFonts.orbitron(textStyle: TextStyle(color: const Color.fromARGB(255, 251, 251, 251))),
                keyboardType: TextInputType.number, // Solo permite números
                decoration: InputDecoration(
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
                  labelText: 'SATURATION TEMPERATURE',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                ),
              )
              )
              ],
              )
              ],
              ),
            ),
            ElevatedButton(
              onPressed: () {
                // Convierte el texto a número (si es válido)
                double? valorA = double.tryParse(_controllerA.text);
                double? valorB = double.tryParse(_controllerB.text);
                double? valorC = double.tryParse(_controllerA.text);
                double? valorT = double.tryParse(_controllerB.text);

                setState(() {
                    // Muestra un mensaje si el valor no es un número válido
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text("Por favor ingrese un número válido")),
                  ); // Un cálculo de ejemplo
                  });
                },  
              child: Text("Calcular"),
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
