#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycam
Version  : 0.6.3
Release  : 4
URL      : https://github.com/SebKuzminsky/pycam/archive/v0.6.3.tar.gz
Source0  : https://github.com/SebKuzminsky/pycam/archive/v0.6.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: pycam-bin = %{version}-%{release}
Requires: pycam-data = %{version}-%{release}
Requires: pycam-license = %{version}-%{release}
Requires: pycam-python = %{version}-%{release}
Requires: enum34
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
Patch1: update.patch

%description
The fonts delivered with PyCAM are taken from QCAD:
http://www.qcad.org/
The fonts are licensed under the GPL v2.0 or later.

%package bin
Summary: bin components for the pycam package.
Group: Binaries
Requires: pycam-data = %{version}-%{release}
Requires: pycam-license = %{version}-%{release}

%description bin
bin components for the pycam package.


%package data
Summary: data components for the pycam package.
Group: Data

%description data
data components for the pycam package.


%package legacypython
Summary: legacypython components for the pycam package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pycam package.


%package license
Summary: license components for the pycam package.
Group: Default

%description license
license components for the pycam package.


%package python
Summary: python components for the pycam package.
Group: Default

%description python
python components for the pycam package.


%prep
%setup -q -n pycam-0.6.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543733464
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycam
cp COPYING.TXT %{buildroot}/usr/share/package-licenses/pycam/COPYING.TXT
cp debian/copyright %{buildroot}/usr/share/package-licenses/pycam/debian_copyright
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pycam
/usr/bin/pycam-cli

%files data
%defattr(-,root,root,-)
/usr/share/pycam/DXF.gpl
/usr/share/pycam/doc/COPYING.TXT
/usr/share/pycam/doc/Changelog
/usr/share/pycam/doc/INSTALL.md
/usr/share/pycam/doc/LICENSE.TXT
/usr/share/pycam/doc/README.md
/usr/share/pycam/doc/release_info.txt
/usr/share/pycam/fonts/README
/usr/share/pycam/fonts/courier.cxf
/usr/share/pycam/fonts/cursive.cxf
/usr/share/pycam/fonts/cyrillic_ii.cxf
/usr/share/pycam/fonts/gothgbt.cxf
/usr/share/pycam/fonts/gothgrt.cxf
/usr/share/pycam/fonts/gothitt.cxf
/usr/share/pycam/fonts/greek_ol.cxf
/usr/share/pycam/fonts/greekc.cxf
/usr/share/pycam/fonts/greekcs.cxf
/usr/share/pycam/fonts/greekp.cxf
/usr/share/pycam/fonts/greeks.cxf
/usr/share/pycam/fonts/hershey.readme
/usr/share/pycam/fonts/iso8859-11.cxf
/usr/share/pycam/fonts/italicc.cxf
/usr/share/pycam/fonts/italiccs.cxf
/usr/share/pycam/fonts/italict.cxf
/usr/share/pycam/fonts/kochigothic.cxf
/usr/share/pycam/fonts/kochimincho.cxf
/usr/share/pycam/fonts/normallatin1.cxf
/usr/share/pycam/fonts/normallatin1.readme
/usr/share/pycam/fonts/normallatin2.cxf
/usr/share/pycam/fonts/romanc.cxf
/usr/share/pycam/fonts/romancs.cxf
/usr/share/pycam/fonts/romand.cxf
/usr/share/pycam/fonts/romanp.cxf
/usr/share/pycam/fonts/romans.cxf
/usr/share/pycam/fonts/romans2.cxf
/usr/share/pycam/fonts/romant.cxf
/usr/share/pycam/fonts/scriptc.cxf
/usr/share/pycam/fonts/scripts.cxf
/usr/share/pycam/fonts/standard.cxf
/usr/share/pycam/fonts/symbol.cxf
/usr/share/pycam/fonts/symbol_astro.cxf
/usr/share/pycam/fonts/symbol_misc1.cxf
/usr/share/pycam/fonts/symbol_misc2.cxf
/usr/share/pycam/fonts/unicode.cxf
/usr/share/pycam/pycam.ico
/usr/share/pycam/samples/Box0+1.stl
/usr/share/pycam/samples/Box0.stl
/usr/share/pycam/samples/Box1.stl
/usr/share/pycam/samples/Box2.stl
/usr/share/pycam/samples/Box3.stl
/usr/share/pycam/samples/SampleScene.stl
/usr/share/pycam/samples/SampleScene2.scad
/usr/share/pycam/samples/SampleScene2.stl
/usr/share/pycam/samples/SampleScene3.scad
/usr/share/pycam/samples/SampleScene3.stl
/usr/share/pycam/samples/Sphere0.stl
/usr/share/pycam/samples/Sphere_cut.scad
/usr/share/pycam/samples/Sphere_cut.stl
/usr/share/pycam/samples/TestModel.stl
/usr/share/pycam/samples/multilayer_engrave.svg
/usr/share/pycam/samples/polygon2.svg
/usr/share/pycam/samples/polygon3.svg
/usr/share/pycam/samples/polygon4.svg
/usr/share/pycam/samples/polygon5.svg
/usr/share/pycam/samples/polygons.svg
/usr/share/pycam/samples/problem_1_triangle.stl
/usr/share/pycam/samples/pycam-text.dxf
/usr/share/pycam/samples/pycam-textbox.scad
/usr/share/pycam/samples/pycam-textbox.stl
/usr/share/pycam/samples/pycam.stl
/usr/share/pycam/samples/pycam_text_2d.svg
/usr/share/pycam/samples/rectangle.svg
/usr/share/pycam/samples/simple-shapes.dxf
/usr/share/pycam/samples/sled.stl
/usr/share/pycam/ui/bounds.ui
/usr/share/pycam/ui/clipboard.ui
/usr/share/pycam/ui/emc_tool_export.ui
/usr/share/pycam/ui/export_settings.ui
/usr/share/pycam/ui/extrusion_chamfer.png
/usr/share/pycam/ui/extrusion_radius_down.png
/usr/share/pycam/ui/extrusion_radius_up.png
/usr/share/pycam/ui/extrusion_sigmoidal.png
/usr/share/pycam/ui/extrusion_sine.png
/usr/share/pycam/ui/fonts.ui
/usr/share/pycam/ui/gtk_console.ui
/usr/share/pycam/ui/gtkrc_windows
/usr/share/pycam/ui/log.ui
/usr/share/pycam/ui/logo_128px.png
/usr/share/pycam/ui/logo_16px.png
/usr/share/pycam/ui/logo_32px.png
/usr/share/pycam/ui/logo_48px.png
/usr/share/pycam/ui/logo_64px.png
/usr/share/pycam/ui/logo_gui.bmp
/usr/share/pycam/ui/logo_gui.png
/usr/share/pycam/ui/logo_gui_vertical.bmp
/usr/share/pycam/ui/logo_scalable.svg
/usr/share/pycam/ui/memory_analyzer.ui
/usr/share/pycam/ui/menubar.xml
/usr/share/pycam/ui/model_export.ui
/usr/share/pycam/ui/model_extrusion.ui
/usr/share/pycam/ui/model_plane_mirror.ui
/usr/share/pycam/ui/model_polygons.ui
/usr/share/pycam/ui/model_position.ui
/usr/share/pycam/ui/model_projection.ui
/usr/share/pycam/ui/model_rotation.ui
/usr/share/pycam/ui/model_scaling.ui
/usr/share/pycam/ui/model_support.ui
/usr/share/pycam/ui/model_support_distributed.ui
/usr/share/pycam/ui/model_support_grid.ui
/usr/share/pycam/ui/model_swap_axes.ui
/usr/share/pycam/ui/models.ui
/usr/share/pycam/ui/opengl.ui
/usr/share/pycam/ui/opengl_view_dimension.ui
/usr/share/pycam/ui/opengl_view_grid.ui
/usr/share/pycam/ui/parallel_processing.ui
/usr/share/pycam/ui/plugin_selector.ui
/usr/share/pycam/ui/processes.ui
/usr/share/pycam/ui/progress_bar.ui
/usr/share/pycam/ui/pycam-project.ui
/usr/share/pycam/ui/tasks.ui
/usr/share/pycam/ui/toolpath_crop.ui
/usr/share/pycam/ui/toolpath_export.ui
/usr/share/pycam/ui/toolpath_grid.ui
/usr/share/pycam/ui/toolpath_simulation.ui
/usr/share/pycam/ui/toolpaths.ui
/usr/share/pycam/ui/tools.ui
/usr/share/pycam/ui/units.ui
/usr/share/pycam/ui/visible.svg
/usr/share/pycam/ui/visible_off.svg

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycam/COPYING.TXT
/usr/share/package-licenses/pycam/debian_copyright

%files python
%defattr(-,root,root,-)
