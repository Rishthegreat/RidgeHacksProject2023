available_devices = [
    ('samsung', 'Samsung', [
        ('galaxy-s3', 'Galaxy S3'),
        ('galaxy-s4', 'Galaxy S4'),
        ('galaxy-s5', 'Galaxy S5'),
        ('galaxy-s6', 'Galaxy S6'),
        ('galaxy-s7', 'Galaxy S7'),
        ('galaxy-s8', 'Galaxy S8'),
        ('galaxy-s9', 'Galaxy S9'),
        ('galaxy-s10', 'Galaxy S10'),
        ('galaxy-s20', 'Galaxy S20'),
        ('galaxy-s21', 'Galaxy S21'),
        ('galaxy-s22', 'Galaxy S22'),
        ('galaxy-s23', 'Galaxy S23'),
    ]),
    ('apple', 'Apple', [
        ('iphone-4', 'iPhone 4'),
        ('iphone-5', 'iPhone 5'),
        ('iphone-6', 'iPhone 6'),
        ('iphone-7', 'iPhone 7'),
        ('iphone-8', 'iPhone 8'),
        ('iphone-9', 'iPhone 9'),
        ('iphone-10', 'iPhone 10'),
        ('iphone-11', 'iPhone 11'),
        ('iphone-12', 'iPhone 12'),
        ('iphone-13', 'iPhone 13'),
        ('iphone-14', 'iPhone 14'),
    ]),
    ('google', 'Google', [
        ('pixel-1', 'Pixel 1'),
        ('pixel-2', 'Pixel 2'),
        ('pixel-3', 'Pixel 3'),
        ('pixel-4', 'Pixel 4'),
        ('pixel-5', 'Pixel 5'),
        ('pixel-6', 'Pixel 6'),
        ('pixel-7', 'Pixel 7'),
    ]),
]

available_parts = [
    ('screen', 'Screen'),
    ('battery', 'Battery'),
    ('camera', 'Camera'),
    ('speaker', 'Speaker'),
    ('microphone', 'Microphone'),
    ('charging-port', 'Charging Port'),
]
# part class
class Part:
    def __init__(self, brand, device, part_name):

        # TODO: validate brand, device, part_name
        '''
        if brand not in [brands[0] for brands in available_devices]:
            raise Exception('invalid_brand')
        
        if device not in [devices[0] for devices in available_devices[available_devices.index(brand)]]:
            raise Exception('invalid_device')
        
        if part_name not in [parts[0] for parts in available_parts]:
            raise Exception('invalid_part')
        '''

        self.part_id = f'{brand}-{device}-{part_name}'