class Solution {
    public long taskSchedulerII(int[] tasks, int space) {
        HashMap<Integer,Long> map = new HashMap<>();
        
        long day = 1;
       for(int t : tasks){
           if(map.containsKey(t) && map.get(t)>day-space-1) {
               day = map.get(t) + space+1 ;
           }
           map.put(t,day);
          // System.out.print(day);
           day++;
           
       }
        
        return day-1 ;
        
    }
}