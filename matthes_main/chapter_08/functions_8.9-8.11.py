messages = ["I'll call you back.", "On my way.", "Wanna grab a beer?", "It's fuckin embarassing!", "I'm gonna be a litte late."]
sent_messages = []


def send_messages(outgoing_list):

    outgoing_pending = outgoing_list[:]
        
    while outgoing_pending:

        current_message = outgoing_pending.pop()

        print(f"\nNow sending message: {current_message}")

        sent_messages.append(current_message)

        if current_message in sent_messages:
            print("Message sent.")


def confirm_sent(sent):

    print(f"\nConfirmation of sent messages:\n")

    for message in sent:
        print(message)


if __name__ == "__main__":
    send_messages(messages)
    confirm_sent(sent_messages)

    