import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { FormInputBase } from '../form.model';


@Component({
  selector: 'app-dynamic-form',
  templateUrl: './dynamic-form.component.html',
  styleUrls: ['./dynamic-form.component.css']
})
export class DynamicFormComponent implements OnChanges {
  
  @Input() formFields: FormInputBase<string | boolean>[] | null = [];

  form: FormGroup;

  ngOnChanges(changes: SimpleChanges): void {
    const group = {};

    if (!changes.formFields) {
      return;
    }
    this.formFields = changes.formFields.currentValue;
    this.formFields.forEach((field) => {
      group[field.key] = field.required ? new FormControl(field.value || '', [...field.validators, Validators.required]) : new FormControl(field.value || '', field.validators);
    });
    this.form = new FormGroup(group);
  }
}