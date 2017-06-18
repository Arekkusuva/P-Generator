import shutil
import subprocess as sp
from modules.state import g_state
from modules import structure


def run_command(commands=['']):
    if len(commands):
        i = 0
        commands_line = ''
        for line in commands:
            if i > 0:
                commands_line += '; ' + line
            else:
                commands_line += line
            i += 1
        try:
            output = sp.Popen(commands_line, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            output.wait()
            return output.communicate()[0].decode('utf-8')
        except:
            return None


def ask_question(question='', options=[]):
    if not options:
        return input('\033[94m%s: \033[0m' % question)
    answer = input('\033[94m%s (%s): \033[0m' % (question, '/'.join(options)))
    if answer in options:
        return answer
    return ask_question(question, options)


def run_py(script_path=''):
    run_command(['python3 %s' % script_path])


def init_template_scripts(template_name=''):
    run_py('%s/%s/%s/index.py' % (g_state.get('generator_dir'), g_state.get('templates_dir'), template_name))


def remove_template(template_name=''):
    structure.remove_files(['%s/%s/%s/%s' % (
        g_state.get('projects_path'),
        g_state.get('generator_dir'),
        g_state.get('templates_dir'),
        template_name
    )])
