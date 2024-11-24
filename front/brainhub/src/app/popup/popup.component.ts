import { Component } from '@angular/core';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrl: './popup.component.css'
})
export class PopupComponent {
  selectedOptions: string[] = []; // Initialisez la liste

  addToList(option: string): void {
    if (!this.selectedOptions.includes(option)) {
      this.selectedOptions.push(option); // Ajoutez seulement si l'option n'est pas déjà présente
      console.log(this.selectedOptions); // Vérifiez dans la console si les données s'ajoutent
    }
  }
}
