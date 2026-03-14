from django.dispatch import Signal

published: Signal
unpublished: Signal
page_published: Signal
page_unpublished: Signal
page_slug_changed: Signal
pre_page_move: Signal
post_page_move: Signal
workflow_approved: Signal
workflow_rejected: Signal
workflow_cancelled: Signal
workflow_submitted: Signal
task_approved: Signal
task_rejected: Signal
task_submitted: Signal
task_cancelled: Signal
pre_validate_delete: Signal
copy_for_translation_done: Signal
init_new_page: Signal
