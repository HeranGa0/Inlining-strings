from binaryninja import *

def get_strings_from_noncode_sections(bv):
    strlist = []
    for section in bv.sections.values():
        if not section.semantics == SectionSemantics.ReadOnlyCodeSectionSemantics:
            log_info(str(section))
            strlist.extend(bv.get_strings(section.start, section.end-section.start))
    return strlist

def define_string_type(bv):
    for s in get_strings_from_noncode_sections(bv):
        if len(bv.get_code_refs(s.start)) >= 1:
            bv.define_user_data_var(s.start, Type.array(Type.char(), s.length))


PluginCommand.register("string_type", "for test", define_string_type)





