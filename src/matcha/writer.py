import os
from .track import Track
from .track_point import TrackPoint
from .crthit import CRTHit
from .match_candidate import MatchCandidate
import numpy as np

def write_tracks_to_file(tracks, file_path):
    """
    Write a list of Track instances to a NumPy file 

    Args
    ----
    tracks : list 
        A list of Track instances.
    file_path : str 
        Output path to store the Numpy file. Defaults to current directory if
        file_path does not exist

    Returns:
        None.
    """
    data = {
        'id': [],
        'image_id': [],
        'interaction_id': [],
        'start_x': [],
        'start_y': [],
        'start_z': [],
        'end_x': [],
        'end_y': [],
        'end_z': [],
        'points': [],
        'depositions': []
    }

    # Convert track objects to dictionary of lists
    for track in tracks:
        data['id'].append(track.id)
        data['image_id'].append(track.image_id)
        data['interaction_id'].append(track.interaction_id)
        data['start_x'].append(track.start_x)
        data['start_y'].append(track.start_y)
        data['start_z'].append(track.start_z)
        data['end_x'].append(track.end_x)
        data['end_y'].append(track.end_y)
        data['end_z'].append(track.end_z)
        data['points'].append(track.points)
        data['depositions'].append(track.depositions)
    
    np.save(file_path+'/tracks.npy', data, allow_pickle=True)

def write_crthits_to_file(crthits, file_path):
    """
    Write a list of CRTHit instances to a NumPy file

    Args
    ----
    crthits : list 
        A list of CRTHit instances.
    file_path : str 
        Output path to store the NumPy file. Defaults to current directory if
        file_path does not exist

    Returns:
        None.
    """
    data = {
        'id': [],
        'total_pe': [],
        't0_sec': [],
        't0_ns': [],
        't1_ns': [],
        'position_x': [],
        'position_y': [],
        'position_z': [],
        'error_x': [],
        'error_y': [],
        'error_z': [],
        'plane': [],
        'tagger': [] 
    }
    
    for crthit in crthits:
        data['id'].append(crthit.id)
        data['total_pe'].append(crthit.total_pe)
        data['t0_sec'].append(crthit.t0_sec)
        data['t0_ns'].append(crthit.t0_ns)
        data['t1_ns'].append(crthit.t1_ns)
        data['position_x'].append(crthit.position_x)
        data['position_y'].append(crthit.position_y)
        data['position_z'].append(crthit.position_z)
        data['error_x'].append(crthit.error_x)
        data['error_y'].append(crthit.error_y)
        data['error_z'].append(crthit.error_z)
        data['plane'].append(crthit.plane)
        data['tagger'].append(crthit.tagger)
    
    np.save(file_path+'/crthits.npy', data, allow_pickle=True)

def write_match_candidates_to_file(match_candidates, file_path):
    """
    Write a list of MatchCandidate instances to a NumPy file. Raises a
    ValueError if the match_candidates list is empty.

    Args
    ----
    match_candidates : list 
        A list of Track instances.
    file_path : str 
        Output path to store the Numpy file. Defaults to current directory if
        file_path does not exist

    Returns:
        None.
    """
    if not match_candidates:
        raise ValueError("Match candidates list is empty")

    data = {
        'track': [],
        'crthit': [],
        'distance_of_closest_approach': []
    }

    for match_candidate in match_candidates:
        data['track'].append(match_candidate.track)
        data['crthit'].append(match_candidate.crthit)
        data['distance_of_closest_approach'].append(match_candidate.distance_of_closest_approach)

    np.save(file_path+'/match_candidates.npy', data, allow_pickle=True)

def write_to_file(tracks, crthits, match_candidates=[], file_path='.'):
    if not os.path.exists(file_path):
        print('WARNING Output file path', file_path, 'does not exist. Defaulting to current directory')
        file_path = ''
    print('Saving matcha class files to', file_path)
    write_tracks_to_file(tracks, file_path)
    write_crthits_to_file(crthits, file_path)
    write_match_candidates_to_file(match_candidates, file_path)
    print('Done saving')



