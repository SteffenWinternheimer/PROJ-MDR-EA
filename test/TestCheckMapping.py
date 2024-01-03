import unittest

from src.check_mapping import check_mapping


class TestCheckMapping(unittest.TestCase):
    def setUp(self):
        print("\nStarting Unittest.\n")

    def tearDown(self):
        print("\nEnding Unittest\n")

    def test_check_mapping(self):
        rule_ids = [
            55, 66, 70, 71, 73, 74, 75, 76, 77, 82, 83, 84, 85, 86, 87, 88, 89, 99, 100, 237, 238, 245, 246, 247, 248,
            250, 310, 330, 495, 612, 778, 811, 816, 857, 862, 895, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610,
            1611, 1612, 1613, 1615, 1984, 1995, 1996, 2013, 2014, 2015, 2016, 2024, 2025, 2026, 2027, 2116, 2117,
            4014, 4027, 4044, 4226, 4228, 4229, 4230, 4231, 4232, 4233, 4234, 4235, 4236, 4237, 4238, 4239, 4240,
            4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 4250, 4251, 4252, 4253, 4254, 4255, 4256, 4257,
            4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274,
            4275, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4290, 4291,
            4292, 4293, 4294, 4295, 4296, 4297, 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308,
            4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4321, 4322, 4323, 4324, 4325,
            4327, 4328, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344,
            4345, 4346, 4347, 4348, 4349, 4350, 4351, 4352, 4353, 4354, 4355, 4356, 4357, 4358, 4359, 4360, 4361,
            4362, 4363, 4364, 4365, 4366, 4367, 4368, 4369, 4370, 4371, 4372, 4373, 4374, 4375, 4376, 4378, 4379,
            4380, 4381, 4382, 4383, 4384, 4385, 4386, 4387, 4388, 4389, 4390, 4391, 4392, 4393, 4394, 4395, 4396,
            4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4409, 4410, 4411, 4412, 4413,
            4414, 4415, 4416, 4417, 4419, 4420, 4421, 4422, 4423, 4424, 4425, 4426, 4427, 4428, 4429, 4430, 4431,
            4432, 4433, 4434, 4435, 4436, 4437, 4438, 4439, 4440, 4441, 4442, 4443, 4444, 4445, 4446, 4447, 4448,
            4449, 4450, 4451, 4452, 4453, 4454, 4455, 4456, 4457, 4458, 4459, 4460, 4461, 4462, 4463, 4464, 4465,
            4466, 4467, 4468, 4469, 4470, 4471, 4472, 4473, 4474, 4475, 4476, 4477, 4478, 4479, 4480, 4481, 4482,
            4483, 4484, 4485, 4486, 4487, 4488, 4489, 4490, 4491, 4492, 4493, 4494, 4495, 4496, 4497, 4498, 4499,
            4500, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511, 4512, 4513, 4514, 4515, 4516,
            4517, 4518, 4519, 4520, 4521, 4522, 4523, 4524, 4525, 4526, 4527, 4528, 4529, 4530, 4531, 4532, 4573,
            4574, 4575, 4576, 4577, 4578, 4579, 4580, 4581, 4582, 4583, 4584, 4585, 4586, 4587, 4588, 4589, 4590,
            4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4605, 4606, 4607, 4608, 4609, 4610,
            4611, 4612, 4613, 4614, 4615, 4616, 4617, 4618, 4619, 4620, 4621, 4622, 4623, 4624, 4625, 4626, 4627,
            4628, 4629, 4630, 4631, 4632, 4636, 4637, 4638, 4639, 4640, 4641, 4642, 4643, 4644, 4645, 4646, 4647,
            4648, 4649, 4650, 4651, 4652, 4653, 4655, 4656, 4657, 4658, 4659, 4660, 4661, 4662, 4663, 4664, 4665,
            4666, 4667, 4668, 4669, 4670, 4671, 4672, 4673, 4674, 4675, 4676, 4677, 4678, 4679, 4680, 4681
        ]

        satisfied_mitigations, unsatisfied_mitigations = check_mapping("T1059.007", rule_ids)
        print(satisfied_mitigations)
        print(unsatisfied_mitigations)
        self.assertEqual(['M1040'], list(satisfied_mitigations.keys()), "Mitigations not correctly detected")
        self.assertEqual([], list(unsatisfied_mitigations.keys()), "Mitigations not correctly detected")

        rule_ids = [5, 10, 20]

        satisfied_mitigations, unsatisfied_mitigations = check_mapping("T1059.007", rule_ids)
        self.assertEqual([], list(satisfied_mitigations.keys()), "Mitigations not correctly detected")
        self.assertEqual(['M1040'], list(unsatisfied_mitigations.keys()), "Mitigations not correctly detected")

        with self.assertRaises(LookupError):
            check_mapping("T1018", rule_ids)


if __name__ == '__main__':
    unittest.main()
