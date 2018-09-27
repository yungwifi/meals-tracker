//
//  SignupViewController.swift
//  meal-tracker-ios
//
//  Created by Spencer Merryman on 9/5/18.
//  Copyright © 2018 Spencer Merryman. All rights reserved.
//

import Foundation
import UIKit
//import Alamofire

class SignupViewController: UIViewController,UITextFieldDelegate {
    @IBOutlet var usernameTextField:UITextField!
    @IBOutlet var passwordTextField:UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    /*Perform actions when the return key is pressed*/
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        if textField == usernameTextField {
            passwordTextField.becomeFirstResponder()
        } else if textField == passwordTextField {
            signUp(username: usernameTextField.text!, password: passwordTextField.text!)
        }
        return true
    }
    
    /*Signup with username and password*/
    func signUp(username:String,password:String) {
        let params = ["username":username,"password":password] as [String:Any]
        Alamofire.request(API_HOST+"/auth/signup",method:.post,parameters:params).responseData
            { response in switch response.result {
            case .success(let data):
                switch response.response?.statusCode ?? -1 {
                case 200:
                    do {
                        User.current = try JSONDecoder().decode(User.self, from: data)
                        self.usernameTextField.text = ""
                        self.passwordTextField.text = ""
                        self.performSegue(withIdentifier: "signupToInbox", sender: nil)
                    } catch {
                        Helper.showAlert(viewController: self,title: "Oops!",message: error.localizedDescription)
                    }
                case 401:
                    Helper.showAlert(viewController: self, title: "Oops", message: "Username Taken")
                default:
                    Helper.showAlert(viewController: self, title: "Oops", message: "Unexpected Error")
                }
            case .failure(let error):
                Helper.showAlert(viewController: self,title: "Oops!",message: error.localizedDescription)
                }
        }
    }
}
