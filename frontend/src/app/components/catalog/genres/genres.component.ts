import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Genre } from 'src/app/models/book.model';
import { DialogOptions } from 'src/app/shared/dialo.model';
import { DialogService } from 'src/app/shared/dialog.service';
import { FormTextbox } from 'src/app/shared/form.model';
import { GenresService } from './genres.service';

@Component({
  selector: 'app-genres',
  templateUrl: './genres.component.html',
  styleUrls: ['./genres.component.scss']
})
export class GenresComponent {

  genres$: Observable<Genre[]>;

  constructor(private genreService: GenresService, private dialogService: DialogService) { 
    this.genres$ = this.genreService.getAll();
  }

  onAddGenre() {
    let options: DialogOptions = {
      title: 'Add Genre',
      cancelText: 'Cancel',
      confirmText: 'Add',
      formFields: [new FormTextbox({
        key: 'name',
        type: 'text',
        label: 'Genre Name',
        required: true,
      }),]

    }
    this.dialogService.open(options)
  }

}
