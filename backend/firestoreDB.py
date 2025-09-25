import firebase_admin
from firebase_admin import credentials, firestore
from typing import Optional
import os

class FirestoreDB:
    def __init__(self):
        self.firestore_client: Optional[firestore.Client] = None
    
    def get_firestore(self) -> Optional[firestore.Client]:
        """Get the Firestore client instance"""
        return self.firestore_client
    
    def connect(self) -> Optional[firestore.Client]:
        """
        Initialize Firebase connection and return Firestore client
        """
        try:
            
            service_account_path = os.path.join(os.path.dirname(__file__), 'files', 'openHandKey.json')
            
            if not firebase_admin._apps:  # Check if Firebase is already initialized
                cred = credentials.Certificate(service_account_path)
                firebase_admin.initialize_app(cred)
                print("Firebase is initialized")
            else:
                print("Firebase already initialized")
            
            self.firestore_client = firestore.client()
            return self.firestore_client
            
        except FileNotFoundError:
            print(f"Service account key file not found at: {service_account_path}")
            print("Make sure 'openHandKey.json' exists in the 'files' directory")
            return None
        except Exception as ex:
            print("Firebase is not initialized")
            print(f"Error: {ex}")
            return None