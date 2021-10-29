package com.example.scifiname;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.lang.Math;

public class MainActivity extends AppCompatActivity {
    //Defining the widget variables
    EditText firstNameTXT;
    EditText lastNameTXT;
    EditText cityTXT;
    EditText schoolTXT;
    EditText broTXT;
    EditText sisTXT;
    Button generatorBTN;
    TextView output;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firstNameTXT= findViewById(R.id.firstTXT);
        lastNameTXT= findViewById(R.id.lastTXT);
        cityTXT= findViewById(R.id.cityTXT);
        schoolTXT= findViewById(R.id.schoolTXT);
        broTXT= findViewById(R.id.broTXT);
        sisTXT= findViewById(R.id.sisTXT);
        generatorBTN=findViewById(R.id.generator);
        output = findViewById(R.id.output);


        //utilize an onClickListener to connect to the button
        generatorBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                generate();
            }
        });



    }

    //generate the sci fi name
    private void generate(){

        String first = String.valueOf(firstNameTXT.getText());
        String last = String.valueOf(lastNameTXT.getText());
        String city = String.valueOf(cityTXT.getText());
        String school = String.valueOf(schoolTXT.getText());
        String brother = String.valueOf(broTXT.getText());
        String sister = String.valueOf(sisTXT.getText());

        int rF= (int) (Math.random()*firstNameTXT.length());
        int rL= (int) (Math.random()*lastNameTXT.length());
        int rC= (int) (Math.random()*cityTXT.length());
        int rS= (int) (Math.random()*schoolTXT.length());
        int rB= (int) (Math.random()* broTXT.length());
        int rSi= (int) (Math.random()*sisTXT.length());


        //generate scifi first name
        String sciFiFirst = (first.substring(0,rF)+last.substring(rL));



        //generate scifi last name
        String sciFiLast = (city.substring(0,rC)+school.substring(rS));


        //generate scifi home name
        String sciFiHome = (brother.substring(rB)+sister.substring(0,rSi));

        //print out a welcome statement
        output.setText(String.format("Welcome! %s %s from %s",sciFiFirst,sciFiLast,sciFiHome));



    }
}
