import bottle
from bottle import route, run, post, request, auth_basic, abort
import keys_Picloud_S3
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket
import os
import json
#####The folloing two lines could let the REST servers to handle multiple requests##
########################(not necessary for local dev. env.)#########################
# from gevent import monkey
# monkey.patch_all()
##########################################################################################
#####AMAZON KEY, store output files. You might have to write your own import approach#####
##########################################################################################
s3_key = keys_Picloud_S3.amazon_s3_key
s3_secretkey = keys_Picloud_S3.amazon_s3_secretkey
rest_key = keys_Picloud_S3.picloud_api_key
rest_secretkey = keys_Picloud_S3.picloud_api_secretkey
###########################################################################################
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 # (or whatever you want)

import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.ubertool

def check(user, passwd):
    if user == keys_Picloud_S3.picloud_api_key and passwd == keys_Picloud_S3.picloud_api_secretkey:
        return True
    return False

all_result = {}

##################################geneec#############################################
@route('/geneec/<jid>', method='POST') 
@auth_basic(check)
def geneec_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')
    from geneec_rest import gfix
    # print request.json
    result = gfix.geneec2(APPRAT,APPNUM,APSPAC,KOC,METHAF,WETTED,METHOD,AIRFLG,YLOCEN,GRNFLG,GRSIZE,ORCFLG,INCORP,SOL,METHAP,HYDHAP,FOTHAP)

    # if (result):
    all_result[jid]['status']='done'
    all_result[jid]['input']=request.json
    all_result[jid]['result']=result

    return {'user_id':'admin', 'result': result, '_id':jid}
##################################geneec#############################################


##################################przm5#############################################
@route('/przm5/<jid>', method='POST') 
@auth_basic(check)
def przm5_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')

    from przm5_rest import PRZM5_pi_new
    result = PRZM5_pi_new.PRZM5_pi(pfac, snowmelt, evapDepth, 
                                 uslek, uslels, uslep, fieldSize, ireg, slope, hydlength,
                                 canopyHoldup, rootDepth, canopyCover, canopyHeight,
                                 NumberOfFactors, useYears,
                                 USLE_day, USLE_mon, USLE_year, USLE_c, USLE_n, USLE_cn,
                                 firstyear, lastyear,
                                 dayEmerge_text, monthEmerge_text, dayMature_text, monthMature_text, dayHarvest_text, monthHarvest_text, addYearM, addYearH,
                                 irflag, tempflag,
                                 fleach, depletion, rateIrrig,
                                 albedo, bcTemp, Q10Box, soilTempBox1,
                                 numHoriz,
                                 SoilProperty_thick, SoilProperty_compartment, SoilProperty_bulkden, SoilProperty_maxcap, SoilProperty_mincap, SoilProperty_oc, SoilProperty_sand, SoilProperty_clay,
                                 rDepthBox, rDeclineBox, rBypassBox,
                                 eDepthBox, eDeclineBox,
                                 appNumber_year, totalApp,
                                 SpecifyYears, ApplicationTypes, PestAppyDay, PestAppyMon, Rela_a, app_date_type, DepthIncorp, PestAppyRate, localEff, localSpray,
                                 PestDispHarvest,
                                 nchem, convert_Foliar1, parentTo3, deg1To2, foliarHalfLifeBox,
                                 koc_check, Koc,
                                 soilHalfLifeBox,
                                 convertSoil1, convert1to3, convert2to3)
    # if (result):
    all_result[jid]['status']='done'
    all_result[jid]['input']=request.json
    all_result[jid]['result']=result

    # print request.json
    # print all_result
    # print list(ff)[0][0]

    return {'user_id':'admin', 'result': result, '_id':jid}

##################################przm5#############################################


################################# VVWM #############################################
@route('/vvwm/<jid>', method='POST') 
@auth_basic(check)
def vvwm_rest(jid):
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')

    from vvwm_rest import VVWM_pi_new
    result = VVWM_pi_new.VVWM_pi(working_dir,
                                koc_check, Koc, soilHalfLifeBox, soilTempBox1, foliarHalfLifeBox,
                                wc_hl, w_temp, bm_hl, ben_temp, ap_hl, p_ref, h_hl, mwt, vp, sol, Q10Box,
                                convertSoil, convert_Foliar, convertWC, convertBen, convertAP, convertH,
                                deg_check, totalApp,
                                SpecifyYears, ApplicationTypes, PestAppyDay, PestAppyMon, appNumber_year, app_date_type, DepthIncorp, PestAppyRate, localEff, localSpray,
                                scenID,
                                buried, D_over_dx, PRBEN, benthic_depth, porosity, bulk_density, FROC2, DOC2, BNMAS,
                                DFAC, SUSED, CHL, FROC1, DOC1, PLMAS,
                                firstYear, lastyear, vvwmSimType,
                                afield, area, depth_0, depth_max,
                                ReservoirFlowAvgDays)

    all_result[jid]['status']='done'
    all_result[jid]['input']=request.json
    all_result[jid]['result']=result

    return {'user_id':'admin', 'result': result, '_id':jid}

################################# VVWM #############################################

##################################przm##############################################
@route('/przm/<jid>', method='POST') 
@auth_basic(check)

def przm_rest(jid):
    import time
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')

    from przm_rest import PRZM_pi_new
    result = PRZM_pi_new.PRZM_pi(noa, met, inp, run, MM, DD, YY, CAM_f, DEPI_text, Ar_text, EFF, Drft)
    return {'user_id':'admin', 'result': result, '_id':jid}
    
##################################przm##############################################

# ##################################przm_batch##############################################
# result_all=[]
# @route('/przm_batch/<jid>', method='POST') 
# @auth_basic(check)
# def przm_rest(jid):
#     from przm_rest import PRZM_pi_new
#     for k, v in request.json.iteritems():
#         exec '%s = v' % k
#     zz=0
#     for przm_obs_temp in przm_objs:
#         print zz
#         # przm_obs_temp = przm_objs[index]
#         result_temp = PRZM_pi_new.PRZM_pi(przm_obs_temp['NOA'], przm_obs_temp['met_o'], przm_obs_temp['inp_o'], przm_obs_temp['run_o'], przm_obs_temp['MM'], przm_obs_temp['DD'], przm_obs_temp['YY'], przm_obs_temp['CAM_f'], przm_obs_temp['DEPI_text'], przm_obs_temp['Ar_text'], przm_obs_temp['EFF'], przm_obs_temp['Drft'])
#         result_all.append(result_temp)
#         zz=zz+1
#     # element = {"user_id":"admin", "_id":jid, "run_type":'batch', "output_html": 'output_html', "model_object_dict":result_all}
#     # print element
#     # from przm_rest import PRZM_batch_control
#     # result = PRZM_pi_new.PRZM_pi(noa, met, inp, run, MM, DD, YY, CAM_f, DEPI_text, Ar_text, EFF, Drft)

#     return {"user_id":"admin", "result": result_all, "_id":jid}
    
# ##################################przm_batch##############################################


##################################przm_batch##############################################
result_all=[]
@route('/przm_batch/<jid>', method='POST') 
@auth_basic(check)
def przm_rest(jid):
    from przm_rest import PRZM_pi_new
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    zz=0
    for przm_obs_temp in przm_objs:
        print zz
        # przm_obs_temp = przm_objs[index]
        result_temp = PRZM_pi_new.PRZM_pi(przm_obs_temp['NOA'], przm_obs_temp['met_o'], przm_obs_temp['inp_o'], przm_obs_temp['run_o'], przm_obs_temp['MM'], przm_obs_temp['DD'], przm_obs_temp['YY'], przm_obs_temp['CAM_f'], przm_obs_temp['DEPI_text'], przm_obs_temp['Ar_text'], przm_obs_temp['EFF'], przm_obs_temp['Drft'])
        przm_obs_temp['link'] = result_temp[0]
        przm_obs_temp['x_precip'] = [float(i) for i in result_temp[1]]
        przm_obs_temp['x_runoff'] = [float(i) for i in result_temp[2]]
        przm_obs_temp['x_et'] = [float(i) for i in result_temp[3]]
        przm_obs_temp['x_irr'] = [float(i) for i in result_temp[4]]
        przm_obs_temp['x_leachate'] = [float(i)/100000 for i in result_temp[5]]
        przm_obs_temp['x_pre_irr'] = [i+j for i,j in zip(przm_obs_temp['x_precip'], przm_obs_temp['x_irr'])]
        result_all.append(przm_obs_temp)
        zz=zz+1
    element={"user_id":"admin", "_id":jid, "run_type":'batch', "output_html": "", "model_object_dict":result_all}
    db['przm'].save(element)

    # return {"user_id":"admin", "result": result_all, "_id":jid}
    
##################################przm_batch##############################################


##################################exams##############################################
@route('/exams/<jid>', method='POST') 
@auth_basic(check)
def exams_rest(jid):
    import time
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    all_result.setdefault(jid,{}).setdefault('status','none')

    from exams_rest import exams_pi
    result = exams_pi.exams_pi(chem_name, scenarios, met, farm, mw, sol, koc, vp, aem, anm, aqp, tmper, n_ph, ph_out, hl_out)
    return {'user_id':'admin', 'result': result, '_id':jid}
    
##################################przm##############################################

##################File upload####################
@route('/file_upload', method='POST') 
@auth_basic(check)
def file_upload():
    import shutil
    for k, v in request.json.iteritems():
        exec '%s = v' % k

    ##upload file to S3
    conn = S3Connection(s3_key, s3_secretkey)
    bucket = Bucket(conn, model_name)
    k=Key(bucket)
    print src1
    os.chdir(src1)
    k.key=name1
    link='https://s3.amazonaws.com/'+model_name+'/'+name1

    print 'begin upload'
    k.set_contents_from_filename('test.zip')
    k.set_acl('public-read-write')
    print 'end upload'
    src1_up=os.path.abspath(os.path.join(src1, '..'))
    os.chdir(src1_up)
    shutil.rmtree(src1)


##########insert results into mongodb#########################
@route('/save_history', method='POST') 
@auth_basic(check)
def insert_output_html():
    for k, v in request.json.iteritems():
        exec "%s = v" % k
    element={"user_id":"admin", "_id":_id, "run_type":run_type, "output_html": output_html, "model_object_dict":model_object_dict}
    db[model_name].save(element)
    print _id

@route('/update_html', method='POST') 
@auth_basic(check)
def update_output_html():
    for k, v in request.json.iteritems():
        exec "%s = v" % k
    # print request.json
    db[model_name].update({"_id" :_id}, {'$set': {"output_html": output_html}})




###############Check History####################
# @route('/geneec1/job/<jid>') 
# @auth_basic(check)
# def show_res(jid):
#     import json
#     print all_result
#     return all_result[jid]

@route('/ubertool_history/<model_name>/<jid>')
@auth_basic(check)
def get_document(model_name, jid):
    entity = db[model_name].find_one({'_id':jid})
    print entity
    if not entity:
        abort(404, 'No document with jid %s' % jid)
    return entity


@route('/user_history', method='POST')
@auth_basic(check)
def get_user_model_hist():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    hist_all = []
    entity = db[model_name].find({'user_id':user_id}).sort("_id", 1)
    for i in entity:
        hist_all.append(i)
    if not entity:
        abort(404, 'No document with jid %s' % jid)
    return {"hist_all":hist_all}

@route('/get_html_output', method='POST')
@auth_basic(check)
def get_html_output():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    html_output_c = db[model_name].find({"_id" :jid}, {"output_html":1, "_id":0})
    for i in html_output_c:
        # print i
        html_output = i['output_html']
    return {"html_output":html_output}

@route('/get_przm_batch_output', method='POST')
@auth_basic(check)
def get_przm_batch_output():
    for k, v in request.json.iteritems():
        exec '%s = v' % k
    result_output_c = db[model_name].find({"_id" :jid}, {"model_object_dict":1, "_id":0})
    for i in result_output_c:
        # print i
        result = i['model_object_dict']
    return {"result":result}


run(host='localhost', port=7777, debug=True)

# run(host='localhost', port=7777, server='gevent', debug=True)




