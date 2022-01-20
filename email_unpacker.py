import mailbox
import email.utils
import email
import pypff
import os
import string 



def atomise_mbox(in_file_mbox):

    print (in_file_mbox)
    failure = []

    root = in_file_mbox.replace(".mbox", "")

    root = root.replace(folder, new_dest)


    if not os.path.exists(root):
        os.makedirs(root)
    else:
        return


    mbox = mailbox.mbox(mbox_path)

    for msg in mbox:
        try:
            # print (msg.get_content_type(), msg['subject'])
            f_name = subject_cleaner(msg['subject'])
            email_path = os.path.join(root,f_name+".msg")
            with open(email_path, 'w') as out:
                gen = email.generator.Generator(out)
                gen.flatten(msg)
        except:
            failure.append(msg)


    print (f"\nskipped {len(failure)}")


def write_message (fout, msg, document):
    """This writes an 'rfc822' message to a given file in mbox format.
    This assumes that the arguments 'msg' and 'document' were generate
    by the 'mailbox' module. The important thing to remember is that the
    document MUST end with two linefeeds ('\n'). It comes this way from
    the mailbox module, so you don't need to do anything if you want to
    write it unchanged. If you modified the document then be sure that
    it still ends with '\n\n'.
    """
    fout.write (msg.unixfrom)
    for l in msg.headers:
        fout.write (l)
    fout.write ('\x0a')
    fout.write (document)


def subject_cleaner(msg):
    msg = ''.join(filter(lambda x:x in string.printable, msg)) 
    msg = msg.replace("=?utf-8?", "").replace("=?UTF-8?", "").replace("Q?", "").replace("q?", "")
    msg = msg.replace("=", "").replace("?", "_").replace("*", "_").replace("+", "_").replace("/", "_").replace("\n", "").replace("|", "").replace(":", "")
    msg  = msg[0:80]
    return msg
 

def atomise_pst(pst_path):
    open_pst(pst_path)



def open_pst(path):
    opst = pypff.open(path)
    root = opst.get_root_folder()   

def find_all_boxes(folder):
    mboxes = []
    psts = []

    for root, subs, files in os.walk(folder):
        for f in files:
            if f.endswith(".mbox"):
                if os.path.exists(os.path.join(root, f)):
                    mboxes.append(os.path.join(root, f))
            elif f.endswith(".pst"):
                if os.path.exists(os.path.join(root, f)):
                    psts.append(os.path.join(root, f))


    return list(set(mboxes)), list(set(psts))



folder = r"E:\email_for_flora\APP_2020_COVID-19_Email_Ephemera_PAR-43934\PAR_43934_01\Personal emails unzipped"

new_dest = r"E:\email_for_flora\APP_2020_COVID-19_Email_Ephemera_PAR-43934\PAR_43934_01\Personal emails unpacked"

mboxes, psts = find_all_boxes(folder)

for mbox_path in mboxes:
    atomise_mbox(mbox_path)

for pst_path in psts:
    atomise_pst(pst_path)