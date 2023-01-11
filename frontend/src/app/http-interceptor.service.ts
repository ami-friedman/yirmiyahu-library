import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { throwError } from 'rxjs';
import { Observable } from 'rxjs/internal/Observable';
import { catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class HttpInterceptorService implements HttpInterceptor {

  constructor(private snackBar: MatSnackBar) {

  }

  intercept(httpRequest: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return next.handle(httpRequest).pipe(
      catchError((error) => {
        switch (error.status) {
          case 401:
            return this.handleError(``, error);
          case 504:
            return this.handleError(`Cannot reach the server. Please contact Yirmiyahu Library support`, error);
          case 409:
            return this.handleError(``, error);
          case 500:
            return this.handleError(``, error);
          default:
            return this.handleError(`Unhandled error! Retry the operation. If failure continues, contact Yirmiyahu Library support`, error);
      }
    })
    );
  }

  private handleError(message: string, error: any) {
    const finalMessage = message + (error.msg ? error.msg : '')
    this.snackBar.open(finalMessage, '',
           {duration: 3000, 
            horizontalPosition: 'center',
            panelClass: ['red-snackbar'],
            verticalPosition: 'top'})
    console.log(`${finalMessage}`)
    return throwError(() => new Error(finalMessage))
  }
}

