# name-gen

Generate names based on input files specifying language traits.

## Use the Program

To execute the program, you need to provide two arguments: the name of a
language specification file and the number of names you want to generate.

The **name of the specification file** is the name of a YAML file in the `lang/`
folder, extension `.yaml`. Do NOT include the `.yaml`; I'll fix that in the
future.

The **number of names to generate** must be int or convertible to int.

## Language Specification Files

Languages are specified in the `lang/` folder, in the form of a YAML (.yaml)
file. At minimum, a language specification file must contain the following:

- `syllable_structures`: a list of strings which encode the permitted syllable
  structures. Each character in a string encodes a "category," which must be
  defined elsewhere in the specification file. For example, the string CVC
  will be interpreted to select one entry at random from the category "C",
  followed by one entry at random from the category "V", and then one more entry
  at random from the category "C" again.
- `C`, `V`, etc.: These are the categores ("cats"_ that can appear in
  `syllable_structures` strings. It is okay to have unused cats; it is not okay
  to have an undefined cat in a syllable structure. That will most certainly
  cause an error.
- `name_shapes`: A poorly-named field, I apologize. The `name_shapes` is a list
  of ints which specifies the length of a name in syllables. For example, an
  entry like `[2, 1]` specifies that names can be one or two syllables long.
- `separator`: This entry allows you to separate syllables for different
  aesthetics. Whatever the separator is defined as, it is inserted at the end
  of each syllable except for the final one. So if you specify that "@" is the
  separator, then you'll generate names that look like: pa@ku@mi.
