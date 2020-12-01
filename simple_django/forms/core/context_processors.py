mass = []
tracks = [{'track_duration': '3:33', 'name': 'Serendipity'}, {'track_duration': '2:22', 'name': 'track'}]


for elem in range(10):
    mass.append(elem)


def massive_context_processor(request):
    return {
        'massive': mass,
        'tracks': tracks
            }
