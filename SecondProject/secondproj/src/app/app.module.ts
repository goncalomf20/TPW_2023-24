// app.module.ts

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module'; // Import the AppRoutingModule
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';

@NgModule({
    
    declarations: [ ], // Remove AppComponent from the declarations array
    imports: [ BrowserModule, AppRoutingModule, HttpClientModule ],
    providers: [],
    bootstrap: [],
})
export class AppModule {}
