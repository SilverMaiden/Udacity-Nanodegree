require 'rspec'

describe "Return 2 numbers that sum to target" do

  it 'should do something' do
    nums = [2, 7, 11, 15]
    target = 9
    TwoSum.two_sum(nums, target).should == [0,1]
  end
end