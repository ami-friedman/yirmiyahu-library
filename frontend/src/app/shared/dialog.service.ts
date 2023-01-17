import { Injectable } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { map, take } from 'rxjs/operators';
import { DialogOptions } from './dialo.model';
import { DialogComponent } from './dialog/dialog.component';
import { FormInputBase } from './form.model';

@Injectable()
export class DialogService {
  constructor(private dialog: MatDialog) { }
  dialogRef: MatDialogRef<DialogComponent>;
  
  public open(options: DialogOptions) {
    this.dialogRef = this.dialog.open(DialogComponent, {    
         data: {
           title: options.title,
           message: options.message,
           cancelText: options.cancelText,
           confirmText: options.confirmText,
           formFields: options.formFields
         }
    });
  }
  public confirmed(): Observable<any> {
    
    return this.dialogRef.afterClosed().pipe(take(1), map(res => {
        return res;
      }
    ));
  }
}