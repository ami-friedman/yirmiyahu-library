import { FormInputBase } from "./form.model";

export interface DialogOptions {
  title: string;
  message?: string;
  cancelText?: string;
  confirmText?: string;
  formFields?: FormInputBase<string | boolean>[];
}