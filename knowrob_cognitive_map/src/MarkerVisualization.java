package org.knowrob.vis;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Vector;
import java.util.concurrent.ConcurrentHashMap;
import java.util.List;
import java.text.DecimalFormat;

import org.ros.message.Duration;
import org.ros.message.Time;
import org.ros.namespace.GraphName;
import org.ros.node.AbstractNodeMain;
import org.ros.node.ConnectedNode;
import org.ros.node.topic.Publisher;
import org.apache.commons.logging.Log;
import org.knowrob.owl.OWLThing;
import org.knowrob.prolog.PrologInterface;
import org.knowrob.tfmemory.TFMemory;
import org.knowrob.vis.collada_1_4_1.ProfileCOMMON;
import org.knowrob.vis.meshes.CheckerBoardMesh;
import org.knowrob.vis.meshes.ColladaMesh;

import tfjava.StampedTransform;
import visualization_msgs.Marker;
import visualization_msgs.MarkerArray;
import geometry_msgs.Pose;

public void displayMesh(String identifier) {
    //TODO: rewriTe this method DEFINE DIFFERENT COLORS
		float r = 1.0f;
		float g = 0;
		float b = 0;
		float a = 0.5f;
		
		final Marker ref_marker = markersCache.get(identifier);
		if(ref_marker==null){
			System.out.println("Refmarker "+identifier+"does not exist");
			return;
		}
		String m_id = identifier +"_highlight";
		Marker m = markers.get(m_id);
		
		if(m==null) {
			m = node.getTopicMessageFactory().newFromType(visualization_msgs.Marker._TYPE);
		}
		m.getHeader().setFrameId(MarkerVisualization.getReferenceFrame());
		m.setId(ref_marker.getId()+100000);//FIXME This should be safe as long as there are less then 100000 markers. But it should be fixed
		m.setNs(ref_marker.getNs());
		m.setMeshResource(ref_marker.getMeshResource());
		m.setMeshUseEmbeddedMaterials(false);
		m.setAction(0);//Add or change object...
		m.getColor().setR(r);
		m.getColor().setG(g);
		m.getColor().setB(b);
		m.getColor().setA(a);
		m.setPose(ref_marker.getPose());
		m.setScale(ref_marker.getScale());
		m.setType(ref_marker.getType());
		synchronized (markers) {
				markers.put(m_id,m);
		}
		synchronized (markersCache) {
			markersCache.put(m_id,m);
		}
		publishMarkers();
		
		
	}