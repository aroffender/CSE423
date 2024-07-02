'''OpenGL extension OES.texture_border_clamp

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.texture_border_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	OpenGL ES provides only a single clamping wrap mode: CLAMP_TO_EDGE.
	However, the ability to clamp to a constant border color can be
	useful to quickly detect texture coordinates that exceed their
	expected limits or to dummy out any such accesses with transparency
	or a neutral color in tiling or light maps.
	
	This extension defines an additional texture clamping algorithm.
	CLAMP_TO_BORDER_OES clamps texture coordinates at all mipmap levels
	such that NEAREST and LINEAR filters of clamped coordinates return
	only the constant border color. This does not add the ability for
	textures to specify borders using glTexImage2D, but only to clamp
	to a constant border value set using glTexParameter and
	glSamplerParameter.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/texture_border_clamp.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.texture_border_clamp import *
from OpenGL.raw.GLES2.OES.texture_border_clamp import _EXTENSION_NAME

def glInitTextureBorderClampOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glTexParameterIivOES.params size not checked against 'pname'
glTexParameterIivOES=wrapper.wrapper(glTexParameterIivOES).setInputArraySize(
    'params', None
)
# INPUT glTexParameterIuivOES.params size not checked against 'pname'
glTexParameterIuivOES=wrapper.wrapper(glTexParameterIuivOES).setInputArraySize(
    'params', None
)
# INPUT glGetTexParameterIivOES.params size not checked against 'pname'
glGetTexParameterIivOES=wrapper.wrapper(glGetTexParameterIivOES).setInputArraySize(
    'params', None
)
# INPUT glGetTexParameterIuivOES.params size not checked against 'pname'
glGetTexParameterIuivOES=wrapper.wrapper(glGetTexParameterIuivOES).setInputArraySize(
    'params', None
)
# INPUT glSamplerParameterIivOES.param size not checked against 'pname'
glSamplerParameterIivOES=wrapper.wrapper(glSamplerParameterIivOES).setInputArraySize(
    'param', None
)
# INPUT glSamplerParameterIuivOES.param size not checked against 'pname'
glSamplerParameterIuivOES=wrapper.wrapper(glSamplerParameterIuivOES).setInputArraySize(
    'param', None
)
# INPUT glGetSamplerParameterIivOES.params size not checked against 'pname'
glGetSamplerParameterIivOES=wrapper.wrapper(glGetSamplerParameterIivOES).setInputArraySize(
    'params', None
)
# INPUT glGetSamplerParameterIuivOES.params size not checked against 'pname'
glGetSamplerParameterIuivOES=wrapper.wrapper(glGetSamplerParameterIuivOES).setInputArraySize(
    'params', None
)
### END AUTOGENERATED SECTION