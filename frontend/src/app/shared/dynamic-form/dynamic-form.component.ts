import { Component, EventEmitter, Input, OnChanges, OnInit, Output, SimpleChanges } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { FormInputBase } from '../form.model';


@Component({
  selector: 'app-dynamic-form',
  templateUrl: './dynamic-form.component.html',
  styleUrls: ['./dynamic-form.component.scss']
})
export class DynamicFormComponent implements OnChanges {
  
  @Input() formFields: FormInputBase<string | boolean>[] | null = [];
  @Input() confirmButtonText: string = "Save";
  @Input() cancelButtonText: string = "Cancel";

  @Output() formSaved: EventEmitter<any> = new EventEmitter();
  
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

  onSubmit() {
    this.formSaved.emit(this.form.value)
  }

  onCancel() {
    this.formSaved.emit(null)
  }
}