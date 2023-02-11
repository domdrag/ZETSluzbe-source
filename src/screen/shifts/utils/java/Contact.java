package org.test; // buildozer.spec
import android.provider.ContactsContract.Contacts;
import android.provider.ContactsContract.Intents;
import android.app.Activity;
import android.content.Intent;
import android.net.Uri;

public class Contact{
    public static void addContact(Activity pyActivity, String name, String phone){
        Intent intent = new Intent(Intents.SHOW_OR_CREATE_CONTACT, Uri.parse("tel:" + phone));
        intent.putExtra(Intents.EXTRA_FORCE_CREATE, true);
        intent.putExtra(Intents.Insert.NAME, name);
        intent.putExtra(Intents.Insert.PHONE, phone);
        pyActivity.startActivity(intent);	
    }	

}