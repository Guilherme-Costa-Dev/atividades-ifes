package com.example.exercicioaposentadoria

import android.os.Bundle
import android.widget.ArrayAdapter
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import com.example.exercicioaposentadoria.databinding.ActivityMainBinding

const val idadeMasculino = 65L
const val idadeFeminino = 62L

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val itens = listOf("Masculino", "Feminino")
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, itens)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        binding.spinnerSexo.adapter = adapter

        binding.buttonCalcular.setOnClickListener {
            val sexoSelecionado = binding.spinnerSexo.selectedItem as String
            val idade = binding.editTextIdade.text.toString().toLongOrNull()

            if (idade != null) {
                val limite = if (sexoSelecionado == "Masculino") idadeMasculino else idadeFeminino
                val resultado = limite - idade

                binding.txtResultado.text = if (resultado > 0) {
                    "Faltam $resultado anos para você se aposentar"
                } else {
                    "Você já deveria ter se aposentado"
                }
            } else {
                binding.txtResultado.text = "Informe uma idade válida"
            }
        }
    }
}