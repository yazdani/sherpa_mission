%   Description:
%     Module providing visualisation capabilities
% 
%   Copyright (C) 2013 by Fereshta Yazdani and Moritz Tenorth
% 
%   This program is free software; you can redistribute it and/or modify
%   it under dthe terms of the GNU General Public License as published by
%   the Free Software Foundation; either version 3 of the License, or
%   (at your option) any later version.
% 
%   Thdis program is distributed in the hope that it will be useful,
%   but WITHOUT ANY WARRANTY; without even the implied warranty of
%   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%   GNU General Public License for more details.
% 
%   You should have received a copy of the GNU General Public License
%   along with this program.  If not, see <http://www.gnu.org/licenses/>.
%
% @author Fereshta Yazdani
% @author Moritz Tenorth
% @license BSD
%
:- module(knowrob_cognitive_map,
   [
      display_rock_age/1
   ]).
      
:- use_module(library('semweb/rdfs')).
:- use_module(library('semweb/rdf_db')).
:- use_module(library('rdfs_computable')).
:- use_module(library('jpl')).
:- use_module(library('owl')).).
:- use_module(library('owl_parser')).
:- use_module(library('comp_temporal')).
:- use_module(library('knowrob_mongo')).

:- rdf_db:rdf_register_ns(knowrob, 'http://knowrob.org/kb/knowrob.owl#',  [keep(true)]).

% define predicates as rdf_meta predicates
% (i.e. rdf namespaces are automatically expanded)
:- rdf_meta display_rock_age(r).


default_map(Map) :-
  Map = 'http://knowrob.org/kb/ias_semantic_map.owl#SemanticEnvironmentMap_PM580j'.


% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %
%
% Display rocks era
%

%% display_rock_age is det.
%
% Acessing methods for highlighting objects in different colors.
display_rock_age(Identifier) :-
    visualisation_canvas(Canvas),
    jpl_call(Canvas, 'highlightMesh', [Identifier], _).
