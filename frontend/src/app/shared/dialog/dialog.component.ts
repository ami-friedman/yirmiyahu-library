import { Component, Inject, Input, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DialogOptions } from '../dialo.model';
import { FormInputBase } from '../form.model';

@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.css']
})
export class DialogComponent {

  message: string = "Are you sure?"
  confirmButtonText = "Confirm"
  cancelButtonText = "Cancel"
  
  formFields:FormInputBase<string | boolean>[];
  
  constructor(
    @Inject(MAT_DIALOG_DATA) private data: DialogOptions,
    private dialogRef: MatDialogRef<DialogComponent>) {
      if(data){
    this.message = data.message || this.message;
    if (this.message) {
      this.confirmButtonText = data.confirmText || this.confirmButtonText;
      this.cancelButtonText = data.cancelText || this.cancelButtonText;
    }
    if (data.formFields) {
      this.formFields = data.formFields;
    }
    }
  }

  onConfirmClick(formValue: any): void {
    this.dialogRef.close(formValue);
  }

}
