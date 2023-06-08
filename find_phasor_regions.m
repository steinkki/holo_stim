%% Original Function:
% function [N, R] = find_phasor_regions(I)
% % [N, R] = FIND_PHASOR_REGIONS(I) 
% % Sample function that generates ten randomly placed locations to
% % be replaced by function that identifies N locations from image I
% % and populates R matrix of size P x Q x N where R(:,:,n) is the nth
% % region.
% 	N = 10;
% 	rows = size(I, 1);
% 	columns = size(I, 2);
%     
% 	R = zeros(rows, columns, N);
% 
% 	for region_index = 1:N
%         x_loc = fix(floor(10 + rand(1) * (columns - 20)));
%         y_loc = fix(floor(10 + rand(1) * (rows - 20)));
%         
%         for r = -8:8
%             for c = -8:8
%                 if (sqrt(r * r + c * c) < 8)
%                     R(y_loc + r, x_loc + c, region_index) = 1;
%                 end
%             end
%         end
%     end
% end


%% New Phasor:


%Is slidebook calling the matlab script or is it calling the function? This
%is not clear to me.
%Can I have it run stuff before?
%Need to have a way to seperate the odors by type. 

function [N,R,Odor]=find_phasor_regions(I)

  N=1;   %Number of regions to target
  rows = size(I, 1);   %size of the image
  columns = size(I, 2);
  R = zeros(rows, columns, N); %start a array the size of the image.
  Odor='S+'   %Operator should change which odor they want to target.
  for region_index=1:N
      %now I need to feed it each ROI

