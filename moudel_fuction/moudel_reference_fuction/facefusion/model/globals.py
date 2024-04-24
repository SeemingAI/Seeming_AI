from typing import List, Optional

from .typings import VideoMemoryStrategy, FaceSelectorMode, FaceAnalyserOrder, FaceAnalyserAge, FaceAnalyserGender, FaceMaskType, FaceMaskRegion, OutputVideoEncoder, OutputVideoPreset, FaceDetectorModel, FaceRecognizerModel, Padding

# general
source_paths : Optional[List[str]] = None
target_path : Optional[str] = None
output_path : Optional[str] = None

# misc
skip_download : Optional[bool] = None


# execution
execution_providers : List[str] = []
execution_thread_count : Optional[int] = None
execution_queue_count : Optional[int] = None
# memory
video_memory_strategy : Optional[VideoMemoryStrategy] = None
system_memory_limit : Optional[int] = None


# face analyser
face_analyser_order : Optional[FaceAnalyserOrder] = None
face_analyser_age : Optional[FaceAnalyserAge] = None
face_analyser_gender : Optional[FaceAnalyserGender] = None
face_detector_model : Optional[FaceDetectorModel] = None
face_detector_size : Optional[str] = None
face_detector_score : Optional[float] = None
face_recognizer_model : Optional[FaceRecognizerModel] = None

# face selector
face_selector_mode : Optional[FaceSelectorMode] = None
reference_face_position : Optional[int] = None
reference_face_distance : Optional[float] = None
reference_frame_number : Optional[int] = None

# face mask
face_mask_types : Optional[List[FaceMaskType]] = None
face_mask_blur : Optional[float] = None
face_mask_padding : Optional[Padding] = None
face_mask_regions : Optional[List[FaceMaskRegion]] = None


# output creation
output_image_quality : Optional[int] = None
output_video_encoder : Optional[OutputVideoEncoder] = None
output_video_preset : Optional[OutputVideoPreset] = None
output_video_quality : Optional[int] = None
output_video_resolution : Optional[str] = None
output_video_fps : Optional[float] = None
skip_audio : Optional[bool] = None
# frame processors
frame_processors : List[str] = []
