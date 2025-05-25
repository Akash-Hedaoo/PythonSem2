 if len(parts) == 6:
                question = {
                    'subdomain': parts[0],
                    'question': parts[1],
                    'options': parts[2:6],
                    'answer': parts[2]  # Always assume first option is correct
                }
                questions.append(question)