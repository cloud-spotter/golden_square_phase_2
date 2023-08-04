import pytest
from lib.MusicTracker import *

"""
When a new MusicTracker object is created
#__init__ creates a new empty list to store tracks listened to
"""
def test_new_MusicTracker_object_creates_empty_list():
    music_tracker = MusicTracker()
    result = music_tracker.listening_list() 
    assert result == []

"""
2. Given a track 
#add adds this to the listening list 
"""
def test_MusicTracker_adds_track_to_listening_list():
    music_tracker = MusicTracker()
    music_tracker.add("Supermassive Black Hole")
    result = music_tracker.listening_list() 
    assert result == ["Supermassive Black Hole"]

"""
3. Given a track already in the listening list
#add raises an exception instead of adding it to the list again
"""
def test_raises_exception_rather_than_add_duplicated_track():
    music_tracker = MusicTracker()
    music_tracker.add("Supermassive Black Hole")
    with pytest.raises(Exception) as e:
        result = music_tracker.add("Supermassive Black Hole") 
    error_message = str(e.value)
    assert error_message == "This track is already in your listening list."

"""
4. Given a non-string
#add raises an exception and displays an error messsage
"""
def test_raises_exception_if_non_string_added():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        result = music_tracker.add(7) 
    error_message = str(e.value)
    assert error_message == "Please enter a string."

"""
5. When called,
#listening_list displays the list of tracks listened to
"""
def test_listening_list_displays_multiple_tracks():
    music_tracker = MusicTracker()
    music_tracker.add("Supermassive Black Hole")
    music_tracker.add("Blackbird")
    music_tracker.add("Take the A Train")
    result = music_tracker.listening_list() 
    assert result == ["Supermassive Black Hole", "Blackbird", "Take the A Train"]