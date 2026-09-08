# Exact equality research checkpoint

Date: 2026-09-08. Active objective: prove nu(k)=B(k) for every k>=0.

## Goal and verified baseline

The exact objective is not replaced by asymptotic equality, a new leading
coefficient, an improved finite upper bound, or a conditional compiler.
The current sources prove the lower bound B(k) and retain attaining words
through k=18. The newly supplied optimal words were independently verified:

    nu(17)=B(17)=24313.
    nu(18)=B(18)=48623.
    92381=B(19)<=nu(19)<=94161.

No all-dimensional exact construction is established. The coefficient-one
manuscript remains a proposed asymptotic proof with internal reviews.
The preceding conversation concerned calibration and repository publication.
The exact research results below are progress; the all-k goal remains active.

The current verified gaps at17and18 are zero; at19 it is1780. The strongest internally reviewed
height-adaptive rate is now exp[-.93(k(log k)²)^(1/5)] above
2^131073+1, with additional exact finite certificates at specified pairs,
superseding the earlier quantitative routes.
Exact equality in ALL dimensions is still not established. Older finite
comparisons below are historical. The supplied24313word supersedes all
previous17upper bounds, including the formerly best verified24658word.

All mathematical execution is restricted to ssh h100. Local operations
are document reading/editing and file handling.

## Latest progress: exact18 breakthrough and initialized-state lifting

The supplied answers/k18_optimal48623.word independently passes root's
ending-suffix enumeration and all262143segment-tree witness checks.
SHA:6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5.
Root script:scripts/verify_k18_optimal48623.py; reports/witnesses:
witnesses/k18_optimal48623/. Oneh100run0.289sec30CPU45wall1GiB.

Frontier separately checked607684first-coordinate-occurrence events,
finding every262143target without using suffixrecurrence or segmenttree.
Script:scratch/verify_k18_optimal48623_first_occurrence_20260908.py;
bundle:scratch/k18_optimal48623_first_occurrence_20260908/.
Oneh100run0.550sec30CPU45wall1GiB. The standalone endpoint proof matches
48623, hence exact18 is established independently of PBBS premises.

Mainrecord:K18_OPTIMAL48623_VERIFIED_20260908.md. Master9.27,top,2.1,
GateD,ledger,AppendixB,index and FINITE_BOUNDS are updated. Firstopen19.
GeneralExt_z(A)=1+lambda_k(P_A) passed independent proof. The structural
reconstruction alsoPASSED one1.221sec30CPU45wall1GiBrun: endpoint689to8881,
profile(6,1^11), recoveredQ85/R24225, reverseRphase1428omits1427/27202,
thenreverseQ. All24310initializedstatescoverbasecube;rank8/9bijections,
allsevenjoinholes, all131071markedrangeORwitnesses, full18rank9oneper
endpointafterfirstthree. Byte-regeneratedfrom17literalwithspecifiedPI.
Proof:scratch/K18_OPTIMAL_INITIALIZED_TWO_CYCLE_STRUCTURE_AND_BYTE_REGENERATION_20260908.md.
Bundle:scratch/k18_optimal_initialized_structure_20260908/.
Rootreadfullsource/proof/report; qualifiedonegeneralrecency-blocksentence
when previousletter iscontainedinlastletter, noactualcaseimpact. No
unprovidedquotient-generatororcanonicalPphaseregenerationclaimed.
The541entrances/exits constraint atB19 was already known fromB18 and
is reconfirmed, not a new numerical result. No one/two-seam19 search.

The forward pruning-prefix method also passes proof review. Mainrecord:
HEIGHT_ADAPTIVE_FORWARD_PREFIX_CERTIFICATE_METHOD_20260908.md,Master9.28.
Actual713certificates for uniform57/87 were not supplied. A local-path
question remains pending. Do not promote the claimed band; currently
verified uniformthresholds remain29/327/1483/6849. Root andinductionread
the entire independent prefixengine before oneh100run. Smallr1..8exact
histograms/cycles/unroundedcharges match oldcensus. Oner163casePASSED:
U/Cat163<.000099417180896906105456651839, proving0.01%for327/328ONLY.
395refinements,14342nodes,13947finalleavesincluding13924unfinished;
priority-freereplaychecksallmass/ceilings. Fullrun0.3283seconds, no retry.
Report:scratch/pbbs_forward_prefix_r163_20260908/forward_prefix_r163_complete_certificate.json.
Proof:scratch/PBBS_FORWARD_PREFIX_R163_ENGINE_AND_REPLAY_SPECIFICATION_20260908.md.
Do not extrapolate this onepair to the713band. No further runauthorized.

This is PROGRESS. The all-k exact goal remains ACTIVE and unproved.

### Other completed scoped results, superseded as18 search routes

- scratch/EXACT_ONE_SEAM_LIFT_PRECEDENCE_AND_ENDPOINT_CAP_THEOREM_20260908.md
  proves the complete one-seam defect/strict-precedence criterion with
  prescribed recency block sizes. Pair-preserving subset caps yield five
  profiles(s,7-s,1^10); all24caps and three17variants were checked in one
  bounded run. Actual18 instead uses an endpoint enlargement and another
  tail, so there is no contradiction.
- scratch/K18_FOUR_END_CUTS_ONE_SEAM_RELABELING_EXACT_GATE_20260908.md
  completely rejects the ten prescribed24309-letter tails formed by four
  endpoint deletions of A or reversal: every defect graph has a directed
  cycle. This excludes any left recency order for those fixed tails,
  not the supplied optimum. The positive standard-lift control passed.
- scratch/EXACT_TWO_SIDED_LIFT_JOINT_RECENCY_COMPILER_AND_SCOPE_20260908.md
  proves the exact whole-target LEFT/RIGHT defect assignment criterion
  with a coupled prefix/suffix block-intersection matrix. Root read full
  proof. It is a general finite compiler, not an exact19route: the older
  run bound forces length>=97234 for this one-unmarked-block architecture.
  Do not run a one/two-seam19search or restart completed18searches.

## Earlier completed turn: exact17 breakthrough, verified18 first lift, uniform finite thresholds

This turn is PROGRESS, including a completed finite case. The all-k goal
remains ACTIVE; do not mark it complete. The first unsettled dimension is
then18, subsequently closed above. Do not continue old17/18word searches
as though those finite cases were open.

### Actual optimal17 word

User file /Users/amir.nuriyev/Downloads/k17_optimal24313.word was copied to
answers/k17_optimal24313.word. SHA:
7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9.
User proof is preserved as scratch/K17_OPTIMAL24313_USER_PROOF_20260908.md.

Root's standalone scripts/verify_k17_optimal24313.py passed every131071
target and every separate segment-tree witness query; length24313,
allnonempty, ordinarynonwrapping, endpointlower24313,gap0. h1000.139sec,
30CPU45wall1GiB. Report and allwitnesses are witnesses/k17_optimal24313/.
Induction independently proved the endpoint lower bound, including N<W,
t=0 and all valid(t+1)-windows; noPBBS needed.

Frontier's separate scratch/verify_k17_optimal24313_direct_forward_20260908.py
passed552396directforwardintervals and all131071targets, withoutsuffix
or tree algorithms. It also reconstructed actualQ85/R24225cycles and
the finalopeningQ||Q0||R||R0||R1. Cyclicfamilies664/130748coverall;
each8setoncein3cyclicletters, each9setoncein4. Openedblocks86/24227
cover639/130747;internalunion131066; missing27299,27303,27315,27319,29363
are supplied by the actual sixletterseam19076,19106,8834|25249,689,12849.
Allshortwindowtableclaims1..5passed. Run0.406sec30CPU45wall1GiB.
Reportsanddirectwitnesses:scratch/k17_optimal24313_forward_20260908/.

Root fully read both verifier sources and all proof audits. Mainrecord:
K17_OPTIMAL24313_VERIFIED_20260908.md; MASTER_HANDOFF9.26,2.1,GateD,
completionledger,AppendixB and topstate updated. The user did NOT supply
the separate1430-rowquotientcertificate or searchgenerator; no regeneration
or14successor-change history is claimed independently replayed. Literal
optimality and the actual two-cycle opening do not require those artifacts.

### Verified18 consequence

Structure constructed the exact trimmed one-coordinate lift, no searches
or deletions: answers/k18_upper48626.word. SHA:
52a68ff6bb2757c00b4be03edbb53eaf821d5dca0985d0a680941502d0c2315b.
All262143targets andrangeORwitnessespassed; exactallrankendpointbound48623.
Report/witnesses:scratch/k18_trimmed_lift_48626_20260908/.
Proof:scratch/K18_VERIFIED_48626_TRIMMED_LIFT_FROM_OPTIMAL_K17_20260908.md.
Rootreadwholeverifier. Run0.832sec30CPU45wall1GiB. Historical18gap3,
subsequently closed by the optimal18word above.
The19/20upperwordsremain94161/188322, gaps1780/3563.

### Uniform finite guarantee audited before the exact17 submission

HEIGHT_ADAPTIVE_UNIFORM_FINITE_THRESHOLDS_20260908.md andMaster9.25
recordnu(k)<1.01WforALLk>=29, <1.001Wfrom327,<1.0001Wfrom1483,
<1.00001Wfrom6849. The signature(Q,U)recursion agrees with prior exact
periodformula; newreciprocalparticlemoment and nonprimitive-topGF yield
decreasingE_r. Two independentproofauditsrootread. Newexactrootbounds
at45/163/741/3424andALL31storedr14..44casespassed; existingcensusSHA
pinned,nofullpartitionrerun. NumericrecordSHA:
acd7d2c2cfc8c067198c3e227c4011de09d32a28df79c41289c0da6fb337ebb4.
This conditionalconstructionbound does not improve the strongest eventual
rate or itself proveexactfiniteattainment.

### Scoped earlier-in-turn architecture results, now historical for17

1. CompleteunrestrictedH3capsCNF (H1/H2frozen,nativeH3triplespreserved,
   noanchors, alllowtargets insidecomponents) is now independentlyUNSAT
   certified. CNFSHA673d26f3dc605da62cdfa335953c1637eb1375f0fee82e85822b68ab4b8747ab.
   Originalsolverprooftruncated; firstDRATcheckfailed. Prefix+emptycandidate
   alsofailed. Delete-before-capturetoyfailed. Cfflush(NULL)whilealive
   fixedproofcapture; toyproofpassed, thenONEidenticalCNF/seed0replay
   (two totalcapdecisions,notone). CompleteproofSHAacfb05ad0054a4824fb3529865b12b7b35ae7c7f76741959ba786e3af6d477ea,
   1450630bytes;officialdrat-trimcommit2e3b2dc0ecf938addbd779d42877b6ed69d9a985
   saysVERIFIED,420originalcoreclauses,215RUPlemmas,720resolutionsteps,
   zeroRATlemmas. GeneratedLRATnotseparatelychecked. Note:
   K17_UNRESTRICTED_TRIPLE_CAPS_INDEPENDENT_DRAT_CERTIFICATE_20260908.md.
   Completeproof/check/corelocalin k17_unrestricted_triple_caps_20260908/
   certificate_export_replay_flushed/. No conflictwithnewoptimalword:
   its chronology and letterinventoryarechanged.
2. FullD^min(h,3)periodicstategraph alsohasuniqueloopfreerouting:
   24310states,146components,4998extraedges,componentDAG andsource
   alternative-matchingSCCsallsingletons. Rootreadfullcode/note.
   PBBS_FULL_CAPPED_RECENCY_AND_MATCHING_GRAPH_OBSTRUCTION_20260908.md.
   AppliesonlyfullDcaps,notarbitraryentrywisecapsornewword.
3. Purefull-recencystarresetlemma andmaximal-capantecedentinterface
   correctasconditionalcompiler. Owner-onlycyclesarethreeunmatchedzeros;
   actualmountainC6examplehas2oldcomponents17/221→2new135/103,notfusion.
   PBBS_FULL_RECENCY_STAR_PORT_TRANSPORT_AND_OWNER_ONLY_GATE_20260908.md.
   No freshbank/wordwasproducedbythisroute. Rootreadfullproof.

All new mathematical jobs have exited. No GitHub push was made. The next
exact goal is the remaining18gap or an all-dimension construction; the
successful17word is the new baseline, not the old cappedPBBS bank.

## Earlier completed turn: exact nonprimitive periods, finite census and construction limits

This turn is PROGRESS. A new user submission was fully audited and
recorded in MASTER_HANDOFF9.24 and
HEIGHT_ADAPTIVE_EXACT_ROTATION_PERIOD_AND_FINITE_CENSUS_20260908.md.
The all-k exact goal remains active, and the verified17upper bound
remains24658. The harmonic0.93general rate remains the strongest
recorded upper estimate; the new census does not improve that exponent.

* Exact translated-return iff and v=lcm_j den(e_(j-1)*sigma_j) passed
  independent proof audit, including all nonprimitive rows, rotation
  sign, sufficiency, bottom case, symmetry-loss divisor, Cartesian root
  count and n physical rotations/root. Full root-read note:
  PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md.
* One independent h100 integer census passed every odd3–101 and even
  lift comparison through102,1,295,970partitions and1,702,866signatures.
  Each signature's n*mass/v is integral; each root/state total is Cat/W.
  All user integer entries and percentage ranges pass. N101 is
  199805614710856411551021117606, relative excess5.9422ppm; B101=W+7,
  so N101−B101=1187277484185535019897543. The1%,0.1%,0.01%ranges
  are29–102,57–102,87–102, eachcasechecked. No hugewordmaterialized.
  Script census_pbbs_exact_rotation_period_partitions_20260908.py;
  report rotation_period_census_20260908/exact_rotation_period_census.json;
  proof PBBS_EXACT_ROTATION_PERIOD_PARTITION_CENSUS_THROUGH101_CERTIFICATE_20260908.md.
  Root andinductionreadfullcode;300CPU360wall4GiB,26.83seconds,exited.
* Root proved andinductionaudited cornerperiod v|lcm(boundaryproducts)
  <=n^q, q<=Q=floor((sqrt(4n−3)−1)/2), hence nativecollarcost
  C_n>=ceil((2Q−1)W/n^Q)>=exp(nlog2−O(sqrtnlogn)). This is a
  TRUE LOWER BOUND for the unchanged word's overhead, notnu−W.
  Sharper analysis of that sameword cannot reachB. Notes:
  PBBS_CORNER_PERIOD_UPPER_BOUND_AND_EXPONENTIAL_COLLAR_BARRIER_AUDIT_20260908.md
  and PBBS_CORNER_PERIOD_BARRIER_SECOND_INDEPENDENT_AUDIT_20260908.md.
* Complete native-D^h recency graph at17 independently reconstructed:
 24310states, both8/9prefixmapsbijections, b9=h. All86972neutral
  candidates tested (nine8subsets/destination plusheightfilter).
  Legal24310native+24310self+17cross; solecomponentedge83→103,
  height3,153→85. Nootherinternaledge, quotientDAG. Crossheight
  cyclesimpossible byprefixcountmonotonicity. Everycyclecoverretains
  eachnativecycleorallitsloops;min146,unique loopfree. Fullroot-read
  proof PBBS_NATIVE_RECENCY_ROUTING_OBSTRUCTION_COMPLETE_AUDIT_20260908.md,
  code audit_k17_native_recency_neutral_graph_20260908.py, complete
  candidate/edge/stateJSONCSV underk17_native_recency_graph_20260908/.
  120CPU150wall2GiB,1.94seconds,exited. Otherclaimedgraphdimensions
  anduserrewriteengineswereNOTreplayed.

The exact-construction work already in progress also completed:

* Canonical H=min(h,3), H1/H2frozen, fullanchors0,3,6,... atH3:
 7414anchors,14720editablepositions,7377blocks,2346272options.
  GlobalminimumPinletterstestprovesALLoptioncombinationstriple8+
  allboundarypair7preservation. Every41225rank1..7target individually
  possible; fixed20943targets,20282unfixed. 4504rank7labelsrequire
  internalpairs,4441uniqueproviderblocks. 1529rank6labelsrequire
  editablefullletters. ExactmenuSHA
  bf55d2ef90e32f7eac6148e1e889d87a4a0214e651adb62df543c2e7af04c642,
  underk17_triple_anchor_menus_20260908/.
* That ONEframe is now PROVABLY IMPOSSIBLE. Initial4441forced7filters
  plus8forcedtargets(63→2,95→37,119→32,125→27,126→2,175→106,
 183→168,55→425) leave2103={1,2,3,5,6,12}withoutanyhost.
  Completeandcompact30blocksuppliercertificates independentlyreplayed
  fromliteralmenus; noHallfloworSATrunneeded. Note
  K17_CANONICAL_W3_ANCHOR_EIGHT_STEP_PROPAGATION_OBSTRUCTION_20260908.md,
  artifacts k17_anchor_propagation_20260908/. 2.93seconds,exited.
  Do not rerun thisrefutedcanonicalframe'sfeasibilitysearch.
* Exact two-letter menus and CNF capbits+forwardwitnessselectors are
  still proved; independent-channel matching is only a necessary
  relaxation, not a construction. Notes PBBS_TRIPLE_PRESERVING_BLOCK_MENUS_AND_COMPACT_SAT_20260908.md
  and PBBS_TWO_LETTER_MENU_COMPATIBILITY_AND_NONMATROID_OBSTRUCTION_20260908.md.
  The recordedindependent-slot counterexample actuallyliesinframeblock0.
* A cappedcommon-contextdirectedcyclefusion lemma is valid: removesame
  unpinnedcoordfromtwoadjacent6letters,groupbyordered(E,F,u),edgesa→v.
  Directedqcycleindistinctcomponentswouldpreserveallwidth<=4palette
  atzeroextras,butlowerpreliminarylossesandlongerupperseamsremain.
  Root'soneexhaustivefixed-bankcensuschecked74562ports,298248literal
  triplecaps,29240contextgroups,andfoundZEROdirectedcycles>=3.
  120CPU150wall2GiB,.621seconds,exited. Note
  K17_CAPPED_RANK6_CONTEXT_PORT_CENSUS_20260908.md;conditionalproof
  PBBS_CAPPED_EQUAL_CONTEXT_DIRECTED_PORT_FUSION_LEMMA_20260908.md.

Next exact action must change an actual restriction: variable anchors,
unrestricted overlapping triple-preserving caps, more general port-state
recoding, or a different owner source. The native full-state inventory,
fullyfrozenpairflow, canonicaleverythirdanchorframe, and thisspecific
one-coordinatecommoncontextcyclefamily are all settled negative decisions.
No broad/randomsearch is authorized; formulate one exactbounded decision
or general constructivelemma before execution. Even a complete cyclic
bank still needs allrankpreservation and a fullycharged linear opening.

All promised userproof/finitechecks andhandoffedits are complete. Allnew
jobs exited; inspectliveagentsbeforeassumingworkisrunning. NoGitHubpush
wasmade. Existingdirtyworktreepreserved. Noall-kexactproofisestablished.

## Latest authoritative state: new rate audits, verified24658 and exact cap decisions

Previous goal turns are PROGRESS: they produced complete exact finite
words/bounds at18–20, new proof audits and quantitative certificates,
and a proved fixed-bank obstruction that changes the next construction.

The actual supplied 24,658-letter word passed root's independent h100
checker: all 131,071 targets and all witnesses separately verified by
range OR. SHA:
24f7f831b7446e942cc0927472296b2d20069f694b8bbad6374e65cc07b6f7fb.
Files: answers/k17_upper24658.word, scripts/verify_k17_upper24658.py,
witnesses/k17_upper24658/, K17_UPPER24658_VERIFIED_20260908.md.
Its 49,316-letter lift at 18 also passed all 262,143 targets; SHA:
abf5fd9f3ee7cd5e66afa777a271077e981ef14a62678b80c0bd52995ed7d37c.
The earlier fixed k19 construction gives 94,161 and its lift to 20 gives
188,322, both fully checked. FINITE_BOUNDS_K18_K19_K20_20260908.md records
B18=48623, B19=92381, B20=184759 and current gaps 693, 1780, 3563.

New full internal proof records (root read complete audits):

* HEIGHT_ADAPTIVE_FRESH_PRIME_RATE_20260908.md: every c<9/512 gives
  eventual error exp(-c k^.2); coefficient 1/128 holds for every
  k>=2^2048+1. The killed reverse geometric process selects distinct
  primes, retains fixed-size conditioning, and bounds primitive failures
  directly. Weaker asymptotics, better onset.
* HEIGHT_ADAPTIVE_DEPTH_PRODUCT_RATE_20260908.md: sharp residue
  discrepancy (1−1/d)rho, finite NB atom 1.001/sqrt(2pi pq), exact
  integral >1.4115874092, product exponent 1.41T, period-tail exponent
  .7T, collar exponent .69T, and parity coefficient 3/5. The audit
  supplies the explicit onset log r>=65536, hence k>=2^131073+1.
* HEIGHT_ADAPTIVE_STOPPED_LCM_RATE_20260908.md: stopped logarithmic
  LCM quota, four-term finite bound, and every eventual c<1/3 on the
  (k log²k)^.2 scale. Root's exact constant checks and the independent
  proof audit pass. Weaker than the depth-product and harmonic routes;
  no optimized onset claimed for this alternative.
* HEIGHT_ADAPTIVE_HARMONIC_PERIOD_RATE_20260908.md: retain the actual
  reciprocal period; n|v changes the candidate cost to a harmonic sum.
  Qr=4(r+1)sqrt(r); the finite Az sum requires integer z. The computable
  four-term inequality is checked at (r,L,M)=(1e12,1100,790),
  (1e14,3500,2250), (1e16,10200,6150), giving relative errors below
  1e−330, 1e−950, 1e−2600 in dimensions 2r+1 and 2r+2. The independent
  outward integer log/root checker uses scale 1e40. Its 1250-cell
  integral sum is exactly 1.074181933864880728. Product exponent
  1.073T and collar exponent 1.069T yield coefficient .93 in both
  parities, with the same explicit onset 2^131073+1. The complete
  probability/parity audit and numerical code/report are linked.

These are internally reviewed deductions on retained finite PBBS inputs,
not external or formal certification. The user's larger checker suites
and search regeneration were not supplied and were not claimed as rerun.
All mathematical execution ran only on h100. No GitHub push was made.
Exact equality remains unproved.

Exact-construction lane, completed before the new rate submissions:

* PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md
  gives the exact arbitrary-interval deficit criterion and the union-of-pins
  criterion for length<=H. Simultaneous assigned targets reduce to unique
  maximal allowed letters; check run endpoints/gaps and each target union.
  Preserving p-owner intersections changes the maximum retained gap to H+2−p.
* K17_CAPPED_PBBS_ALL_LOWER_TARGETS_INDIVIDUAL_HOST_CERTIFICATE_20260908.md:
  In the fixed146 cycles with H=min(h,3), all65535 rank1..8 targets
  have individual hosts. Every coordinate has127 singleton hosts
  (7 at height2, 120 at height3) in44 cycles. The exhaustive70737
  short intervals give915416 hosts; actual caps for all65535 targets
  were independently replayed. Simultaneous coverage is NOT proved.
* K17_CAPPED_LOW_TARGET_FLOW_HALL_OBSTRUCTION_20260908.md:
  Freeze H1/H2. There are22134 H3 positions; all12376 rank6 labels
  must retain a literal occurrence when every native pair OR is preserved.
  The flow demands9401 small targets, but its exact maximum is8245.
  A1768-target Hall family (rank3:17, rank4:238, rank5:1513) has6256
  eligible positions but only612 usable group slots, deficit1156.
  Matching and Hall upper bound were independently replayed without a
  solver. The canonical alternating frame has capacity7013<9401, so
  no second flow was needed. No complete cap of this fixed bank can
  preserve all H3 pairs while H1/H2 stay frozen. This is an architecture
  obstruction, not a lower bound for unrestricted nu(17).

Next exact construction step: allow rank7 pair occurrences to change,
using short-interval witnesses and recovering their targets elsewhere.
Do not retry the now-refuted literal-low-target/fully-frozen-pair flow.
The complete individual host menu is under
scratch/k17_capped_short_hosts_20260908/. No mathematical process remains
live after the bounded jobs.

## Earlier authoritative state: logarithmic-gcd endpoint rate, complete audits, verified24668

Master Sections9.14–9.19 and the top/index/finite table/AppendixB now
record the following completed internally reviewed deductions. Root read
the complete helper proofs and checked the conditioning and constants.
Internal AI review is not external mathematical or formal certification.

1. HEIGHT_ADAPTIVE_PERIOD_BOUNDS_20260908.md consolidates nd|v,
   synchronous primitive-row descent, the one-row rational beta bound,
   exact thresholds5643/6255, and explicit superpolynomial c2^-32 above
   ceil(exp(exp256)). The beta threshold checks ran onh100 with exact
   rational arithmetic; no floating-point premise.
2. HEIGHT_ADAPTIVE_PROFILE_SIEVE_RATE_20260908.md proves the exact
   every-third conditional profile law and maximal atom1024/sqrt(m),
   original-law missing-prime second-moment sieve, and explicit rate
   exp[-2^-50 k^(1/7)(loglog k/log k)^(6/7)] above
   ceil(exp(exp(2^21))). Do not condition free laws on regularity or
   primitivity. Full local, prime and probability audits are saved.
3. HEIGHT_ADAPTIVE_MULTILEVEL_PROFILE_BOUND_20260908.md proves the
   fixed-size joint-profile atom via an exactly normalized Boltzmann
   mixture, finite delta with all proposed constants, divisor-tuple
   averaging and exp[-c log k loglog k] for c<1/(2log2). It also records
   the upper return time M=lcm_s(n_s n_(s+1)); all physical periods are
   odd, f/f² periods agree, and when every row is primitive v=M.
4. HEIGHT_ADAPTIVE_REVERSE_PROFILE_RATE_20260908.md is the preceding
   one-fifth rate. Exact reverse NB tails concentrate original second differences
   after explicitly paying fixed-size conditioning. Existence of one
   good completion bounds the FULL free law by2^20/sqrt(m). With
   Gamma=r^(1/5)(logr)^(-3/5),L=floorGamma·logr, good-event failure is
   <=exp(-2^-26Gamma²) onloglogr>=2^20. The first-moment sieve uses
   B0=2^256,delta2^-40,a2^-320; at most6selected primes divide any
   integer in the full conditional support. Candidate union/charge
   gives explicitc2^-330 for allk>=ceil(exp(exp(2^21))). No unknown
   constant or unspecified threshold remains in this conservative form.
5. HEIGHT_ADAPTIVE_FRACTIONAL_LCM_BOUND_20260908.md gives the uniform
   finite fractional moment with exponent96(2L/logL)^(1/beta), then
   exp[-c(logk)²] for c<1/(6144e²), includingc1/65536. It is stronger
   than the logk·loglogk alternative but weaker than both stretched-
   exponential rates. No finite starting dimension is certified for it.
6. HEIGHT_ADAPTIVE_LOG_GCD_RATE_20260908.md is now strongest:
   nu/W<=1+exp[-(k(log k)^2)^(1/5)/128] for every
   k>=ceil(exp(exp(2^21))), also<=1+exp[-k^(1/5)] on that domain.
   Same word and finite corridor/pruning inputs. Under P* the whole
   incoming row is iid geometric after summing its NB mass; odd-row
   nonprimitive probability<=p exp(-2pq/3), so no separate ell-regularity
   event is needed. The log-gcd lemma for unimodal possibly infinite U is
   P(2U+1|v)<=[log(2+log v)+20+2rho log v]/log Y0.
   With J=(r(log r)^2)^(1/5), L=floor J, coarse child ranges give pass<=1/2
   for candidates v<=exp(L/16) on loglog r>=2^20. Successive conditional
   expectations give P*(A,all L tests)<=2^-L; pay Q_r once. No independence
   of profile sizes and no primitive-conditioned kernel is asserted.
   Explicit bad<=exp(-L), short period<=exp(-L/3), collar<=exp(-L/32),
   and parity L>=J(k)/4 give coefficient1/128. All three complete audits
   and the root synthesis are saved and read. This gains a factor log k
   over item4, and still does not imply exact equality.

New literal checks, all executed only onh100 with90CPU/110wall/1GiB caps:

    answers/k17_upper24715.word: PASS all131071targets and witnesses;
    SHA3e7da8c69f8d32ca73750e12b8746fc483f9d56a441ad94f1d3a2e9b4c11b2fe.
    answers/k17_upper24668.word: PASS all131071targets and witnesses;
    SHA22af061610f9c6cb4708ccca77c8d8008f251a1cc40f92858ca79bf7ad2ffff6.

Each has a standalone scripts/verify_k17_upperNNNNN.py, exact report
and allzero-based inclusive witnesses underwitnesses/k17_upperNNNNN/.
The24668record isK17_UPPER24668_VERIFIED_20260908.md. It saves47against
24715and leaves355toB17. Userrewrite/search sources were not supplied;
the literalwordchecks suffice and are independent of PBBS inputs.
The specifiedDownloads/k17_upper24660.word was absent. Only its pasted
claim and sandboxlink are available; no independent24660check occurred.

Intermediate exact-construction progress this turn is also retained:

- K17_HEIGHT_ADAPTIVE24947_OPTIMAL_BINARY_FOREST_REPAIR_20260908.md:
  the canonical24829prefix plus118leafrepair gives24947. Exactly10
  eligibleparents exist and all10canbeused; optimality is only within
  the fixed128-hole binaryforest model. Complete literalcheckpassed.
- PBBS_HEIGHT_ADAPTIVE_COLLAR_OVERLAP_AND_COMMON_CONTEXT_GRAFT_OBSTRUCTIONS_20260908.md:
  different-height native erosion words have no nonempty literaloverlap;
  same-height differentcycles overlap atmostH−1. Openedblocks gluedonly
  byliteraloverlaps retain≥W+sum c_H H+sumoccupied(H−1), at17=24857.
  Nonidentitycommon(H−1)-context seamgrafts cannot preserve allunique
  middleowners. These are architecture limits, not unrestrictedbounds.
- PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md:
  capH=min(h,3) givescyclicallranks6..17 andnolowerranks; runendpoints
  mustremain andkept-occurrencegaps≤H+1 are exactowner-preservingcaps.
  AtB17every4letterORmusthaverank≥9, so no4unchangedconsecutiveletters
  fromnativeh≥4periodscanoccur. Higher-h H3positionshavetwodistinctpins
  and cannot hostsingletons. Simultaneouslowercoverage remainsopen.

No further construction search is running. No new GitHub push was made.
This goal continuation made concrete proof and finite progress; exact
equality remains active and must not be marked complete.

## Earlier authoritative state: polynomial rate and verified24957

The user's height-adaptive construction has completed internal proof
review. Main consolidated record:

    HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md.

For oddn=2r+1>=3 it proves

    nu(n)<=W_r+floor((2^(n+1)-3W_r)/n).

The even lift doubles the original odd upper bound and width exactly.
Consequently the relative error is sqrt(2pi/k)+O(1/k), with exact
thresholds569 for factor1.1 and62233 for factor1.01. The finite
global-maximum corridor can be chosen at a maximum preceded by a nonempty
reverse-Dyck gap, giving height>=q+1 for every NONEMPTY rank(r-q) target.
The exact one-step map preserves height, so the lower interleaved cycle
has the same height. Choosing each cycle's own height as aperture gives
nonzero erosion, all-rank coverage and costW+sum_cycles(2h-1).
The equality-edge residue proves every cycle length divisible byn;
reflection gives sum_middle(range)=2^n-W and the explicit formula.

Complete proof/audit files:

- PBBS_STRICT_HEIGHT_CORRIDOR_AND_INTERLEAVED_HEIGHT_INDEPENDENT_AUDIT_20260908.md
- PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md
- HEIGHT_ADAPTIVE_PBBS_ROOT_SYNTHESIS_INDEPENDENT_AUDIT_20260908.md

Root read both full proofs, the retained global-maximum corridor proof,
and the deterministic generator. This route uses finite matching and
residence identities; it does not depend on the clock, renewal, overlap
or diagonal proofs. Internal review is not external/formal certification.

One fixed canonicalh100 construction (minimum-mask cuts, cycles ordered
by minima, no search) has146cycles and height sum519. It produced:

    theorem25202: all131071targets;
    trimmed24829:130943targets,128holes(65rank10,49rank11,14rank12);
    repaired24957: append all128holes, all131071targets.

The full word was additionally checked by a separate root-owned suffix
enumeration and all131071witnesses independently replayed by range OR.
Current word/hash:

    answers/k17_upper24957.word
    dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db

Script scripts/verify_k17_upper24957.py; root reports and all witnesses
in witnesses/k17_upper24957/. Full generation bundle is
scratch/k17_height_adaptive_20260908/ and its record
K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md.
The user's claimed24969word/140holes was not supplied: our different fixed
cuts/order gave128holes, without optimization. This is not a contradiction
because boundary witnesses depend on cuts and component order.

The user also supplied Downloads/k17_upper25374.word. It separately PASSED
root's independent checker, hash16951cef9e2efff841c6bbf9cc72f2061f35650dda850714fcceee7a7bb43208.
It is retained with complete certificates in answers/ and
witnesses/k17_upper25374/. Its intermediate matching/Hall/deletion search
certificates were not supplied, and are not needed for the literal bound.
The24957word saves417against25374 and788against25745.

Before this, the inverse-logarithmic argument was fully audited with
C=2^400000 and thresholdceil(exp(exp(4194304))). It is recorded in
COEFFICIENT_ONE_INVERSE_LOG_RATE_20260908.md and master9.10, with its
geometric PGF and original-composition transfer proofs. It is now a
superseded but valid quantitative record, not pending work.

The native291 extension lane also advanced: exactly20 additional letters
give all17singletons,308rank8/9targets and1979total targets. The311word
is optimal for its own family;20is minimal under the retained rank8triple
condition. It has37 repeated below8incidences, forcing at least16638more
flat steps in any exact-bound full completion of that prefix. All scripts
and witnesses are saved; no further extension search is running.

Master9.10–9.13, its current finite table and AppendixB are updated.
All new mathematical jobs have completed. No GitHub push was made.

## Earlier native-block and logarithmic-rate record

The user supplied a concrete 35-letter periodic word. One bounded exact
h100 replay verified all eight rotations, their zero-letter alternating
fusion into a 280-cycle, and the prescribed linear openings. The resulting
named target families have exact linear minima38,283,291:

| Family | Targets | Rank-nine targets | Targets below nine | Optimal length |
|---|---:|---:|---:|---:|
| Base cycle family | 251 | 35 | 105 | 38 |
| Eight-cycle union | 1811 | 280 | 807 | 283 |
| Rooted word family | 1876 | 288 | 836 | 291 |

Thus the user's21-position saving is verified. The rooted291 also attains
the endpoint lower bound for its own family, an additional deduction.
Its288 four-windows are distinct rank-nine owners, and it has288 distinct
rank-eight triple targets. All280 native recency states remain literal.
At rank nine its budget identity is291-288=0+3+0. It is a candidate native
block/prefix for the exact route, not a full-cube construction.

Authoritative record and literal artifacts:

- `USER_NATIVE35_GRAFT280_AND_ROOTED291_INDEPENDENT_CERTIFICATE_20260908.md`
- `native35_user_graft_20260908/native283_joint_optimal_linear.word`
- `native35_user_graft_20260908/native291_rooted_word.word`
- `native35_user_graft_20260908/native35_graft_certificate.json`
- `native35_user_graft_20260908/native35_graft_targets_and_witnesses.json`
- `verify_user_native35_recency_graft_20260908.py`

The user's separately mentioned24313-state static inventory was NOT
supplied or checked. Do not promote its coverage or isolated-state claim
to an independently verified result.

The global recency potential is proved:
N-D_s=L_s+b_s(P_N)+E_s, starting from the empty state. Increases of b_s
are unit increases and cannot introduce a new rank-s target. This rules
out using all six earlier biclique transitions in ANY exact k17 word,
not only the flat bank: they alone giveL9>=6. See
`RECENCY_RANK_BUDGET_AND_SIXWAY_PORT_COST_INDEPENDENT_AUDIT_20260908.md`.
The user's native alternating cycle has no such rank-nine charge.

The strongest quantitative rate is now fully recorded in master9.8 and
`COEFFICIENT_ONE_SHARP_TAIL_RATE_20260908.md`. With A=2^2097152 and
k*=ceil(exp(exp(2^1048616))), for every k>=k*:

    nu/W <=1+2^76 (loglog k)^(3/2+2^-1048577)
                        /(log k)^(2^-1048577),
    nu/W <=1+(log k)^(-2^-1048578).

These are internally reviewed numerical deductions on the finite PBBS
inputs. The unconditional finite exterior estimate has constant32 and
Gaussian exponent-H²/(r+1/2), with rationalTheta refinement; the specified
r1000,H120 check onh100 certifies an upper bound<1/25000. Records:
`SHARP_PRODUCT_SCD_EXTERIOR_BOUND_INDEPENDENT_AUDIT_20260908.md` and
`PBBS_SHRINKING_WINDOW_SHARP_RATE_COMPLETE_INDEPENDENT_AUDIT_20260908.md`.
The earlier rate sections9.5 and9.7 remain valid but are superseded by9.8.

Exact equality remains unproved. This earlier native-block check itself
did not improve the then-current finite interval; the later height-adaptive
24957 result above is now authoritative.
The completed native-block and tail checks were not broad/random searches.
No new changes have been pushed to GitHub in this continuation.

## Parallel exact construction lane: 1513-sector bank

The original components 0 through 8 now form one 1513-owner GOOD cycle;
the fixed 306-owner prefix is unchanged, and 132 GOOD cycles remain.
All proper upper support and the rank-eight adjacency counter survive.
The two latest fusions preserve exact local rank-seven pair and rank-six
letter counters. All rank-seven targets are supplied by 19,346 good pair
targets and the original 102 protected prefix targets; all 12,376 rank-six
targets occur as good letters. No simultaneous host assignment or linear
opening has been supplied. The 221-parent (6,1) family is exhausted:
all its endpoints lie inside the 1513 sector, even if temporary splits
are allowed. The two rank-eight holes also remain and at least one needs
a new internal Q adjacency; counter-preserving moves alone cannot finish.

Current authoritative records:

- `K17_NINE_COMPONENT_1513_FUSION_AND_PARENT_FAMILY_SATURATION_20260908.md`
- `K17_LOWER_BANK_FINAL_1513_INCREMENTAL_AUDIT_20260908.md`
- `k17_1513_sector_fusion_20260908/`

The all-r short-sector path now preserves ALL upper ranks by proof,
including the untouched height-three and maximum-height corridors and
explicit immediate-upper recaptures. See
`PBBS_GLOBAL_CORRIDOR_HEIGHT_AND_SHORT_SECTOR_FULL_UPPER_PRESERVATION_20260908.md`
and its independent audit. This supersedes earlier upper-support caveats
below; arbitrary-dimensional facet injectivity remains unproved.

The user's arbitrary-endpoint deficit/full-window-block theorem also
passes pure-proof review, recorded in
`ARBITRARY_ENDPOINT_DEFICIT_AND_FULL_WIDTH_BLOCK_INDEPENDENT_AUDIT_20260908.md`.
At k17 it forces 16,909 distinct rank-nine four-windows and witness-length
order 1,2,3,4,3,2,1, with at most six missing consecutive-owner-union
targets in EACH upper rank. These are necessities, not a construction.

The user's first quantitative PBBS rate has now been numerically audited
and recorded in MASTER_HANDOFF section 9.5 and the root file
`COEFFICIENT_ONE_EXPLICIT_RATE_20260908.md`. Explicit choices are
A=2^2097152, gamma=2^-2097160, C=1 beyond
k0=ceil(exp(exp(2^2097165))). A version for every k>=2 has C=2^60.
The source review transcription is `USER_PBBS_QUANTITATIVE_RATE_CLAIM_20260908.md`.
These are conservative internal proof constants, retaining the inherited
PBBS manuscript's proposed-proof status. They do not improve k17.

The subsequent six-way recency-state gadget and coherent-class fusion
theorem pass pure-proof audit and are recorded in master section 9.6.
Their ports are absent from the present source and cannot be created
inside its protected flat four-window schedule. See
`RECENCY_BICLIQUE_AND_COHERENT_CLASS_FUSION_INDEPENDENT_AUDIT_20260908.md`
and `K17_SIXWAY_RECENCY_PORT_OBSTRUCTION_IN_CURRENT_FLAT_BANK_20260908.md`.

The subsequent terminal and sharp-tail audits are complete and recorded
above. A sparse three-way recency interface also passed pure-proof review:
`K17_SPARSE_RECENCY_C6_WITH_FLAT_FOUR_WINDOW_PORTS_20260908.md`.
It has exact width1-through4 transfer, twelve distinct local middle owners
and facets, and literal Johnson predecessor/successor strips. Its ports
are not embedded and require changing the current rank-seven pair row.
The more general complete-class obstruction is
`K17_FLAT_COHERENT_CLASS_FACET_BUDGET_OBSTRUCTION_20260908.md`.
Neither conditional connector replaces the all-k equality objective.

## Replacement Johnson prefix and its original baseline

The active k17 source component is now

    badsix_allports_johnson_306_owner_path.word
    badsix_allports_johnson_308_depth2_source.word.

The former relaxed prefix with three non-Johnson seams is ruled out for
the proposed one-pivot schedule. Do not resume constructing Q around that
old prefix. The new prefix supersedes it and passes that obstruction.

The exact replacement uses the same six 51-cycles, but all 51 cuts rather
than the earlier 17 individually safe cuts. The complete 612-option
decision finds a path with ZERO non-Johnson seams and ZERO prefix-internal
rank-eight duplicates. Its order/cuts, all forward, are

    116/33, 118/32, 122/31, 129/30, 138/29, 115/0.

The source has 308 letters, minimum letter rank seven, and exact depth-two
replay. With the other 140 canonical cycles intact, it retains all 41,225
proper upper targets, including all 102 targets supported only by the six
bad cycles. Its global adjacent rank-eight palette has only two holes,
43857 and 46420, and one duplicate involving an outside cycle. These facts
were checked on h100 and the complete DP certificate is retained.

Records:

* `K17_PBBS_ALLPORTS_JOHNSON_306_OWNER_PREFIX_20260908.md`
* `decide_k17_pbbs_badsix_all_ports_20260908.py`
* `k17_pbbs_badsix_allports_johnson_decision_20260908.json`
* `K17_PBBS_ALLPORTS_JOHNSON_PREFIX_ENDPOINT_INTERFACE_20260908.md`

The new endpoint interface proves that neither hole occurs anywhere in
the 308-letter source or can use the initial, pivot, or P/Q exception.
At most one can use the final suffix. Hence at least one of the two must
be recreated by an adjacency strictly inside Q. Each has seven remaining
rank-nine superowners. A chosen provider edge must subsequently retain
its literal lower witness in the common-cap compiler.
The five new prefix seams also earn zero credit against the 59 globally
private rank-ten colors forced by the unsafe reference cycles. The
unchanged final owner excludes pivot and P/Q credit. Thus at least 59
new rank-ten adjacency colors are required strictly inside Q, even under
arbitrary Q rethreading. Section 8 of the current interface supplies the
separate bounded check and exact scope.

The new prefix still requires 24,004 remaining owners in a compatible Q,
all upper witnesses after joining, and the full lower common-cap assignment.
It is a source component, not a 24,313-letter universal word.

The replacement now has a proved all-r formula, not just the k17 search
certificate. See `PBBS_ALL_R_SHORT_RUN_SECTOR_JOHNSON_PATH_20260908.md`.
For n=2r+1, r>=3, the canonical boundary-triple components have

    A_b=(b,r-2-b,0,n-1), 0<=b<=r-3, g=f^2.

Traverse the full 3n-cycle from g^(2n-b)A_b for b>0, and from A_0 for
b=0, in block order 1,2,...,r-3,0. This is a Johnson path on all
3(2r+1)(r-2) bad-sector owners, with every internal positive run at
least three. Its maximal depth-two source has two extra letters and
minimum letter rank at least r-1. The proof uses explicit parity forms
and all three f-phase seam tests; root independently checked it. The
bounded r=3,...,10 tests are supporting evidence only.
Full upper-support preservation in all r is now proved in the later
record linked above. Lower-facet injectivity is still only checked in
the k17 instance.

## Additional exact progress in this checkpoint

1. The lower exceptional-facet theorem bounds the number of missing
   adjacency colors by J+2 for the stated consecutive-start schedule with
   J internal depth increases and no final increase. For one pivot,
   b+e<=2, where b counts non-Johnson edges and e repeated facet colors.
   This rules out the previous prefix, whose b=3. The general d-extra-
   position consecutive-start bound is b+e<=d. The old prefix has no
   internal facet duplicate, so that broader bound alone does not rule
   out arbitrary retiming. See
   `K17_PBBS_PREFIX_ONE_PIVOT_NOGO_AND_CONSECUTIVE_START_BUDGET_20260908.md`.

2. `EXACT_B_TWO_SIDED_ADJACENT_PALETTE_REQUIREMENT_20260908.md` proves
   the upper companion to the master's endpoint bound: at most 2d rank-
   (r+1) colors can be absent from consecutive-owner unions. For
   consecutive starts, only J upper exceptions are possible, one per
   strict depth increase. In the one-pivot schedule the only exceptional
   rank-ten physical cell is [305,308]. The note and its independent audit
   derive an exact 59-new-adjacency requirement for the OLD frozen prefix;
   its prefix-specific seam credits must not be silently applied to a
   different prefix. The generic upper theorem remains applicable.

3. `PBBS_CANONICAL_MOUNTAIN_C6_ALL_UPPER_TRANSPORT_20260908.md` gives
   a fully checked local surgery: original cycles 17+221 become 135+103,
   preserving all 1,343 local proper upper targets and the full rank-eight
   adjacency multiset. New positive runs have length at least seven.
   It composes with either disjoint 306-prefix construction. It does not
   fuse the two components or give safe openings: the all-cycle scalar
   recapture bill drops from 129 to 125, while 59 cycles remain unsafe at
   every cut. The exact verifier and complete target-transport map are
   `audit_k17_canonical_rigid_clean_c6_20260908.py` and
   `k17_canonical_rigid_clean_c6_20260908.json`.

4. `EXACT_B_TAGGED_MODULE_SECTOR_MOMENTS_AND_LOWER_CAP_BURDEN_20260908.md`
   gives exact mixed-hub sector equations for the separate tagged route.
   At k17 a seven/eight-period mixture would require 429 modules of each
   type and nonuniform core incidences. At k19 the fixed-three-hub,
   width-four scheme fails divisibility. The k17 unmodified width-three
   deck forces 1,287 repeated facet occurrences. A legal pulse cap changes
   precisely 1,287 single-hub cells without altering middle or upper
   windows. However, the protected-endpoint lemma proves that a frozen
   flat owner chronology still cannot reach equality: shrinking deletes
   an occurrence but cannot make that endpoint serve a different facet.
   With the stated single-opening assumptions the resulting architecture
   has lower bounds 25,594 (envelope/collared owner pair) or 25,593 (bare
   owner pair), far above B(17). The pulse is not a completion escape.
   New owner transitions or a different module/schedule are required.

## New exact restrictions

1. `EXACT_B_CRITICAL_INTERVAL_RIGIDITY_20260908.md` applies the deadline
   argument to ALL inclusion-minimal intervals whose OR reaches the middle
   rank. If p counts them, then

       W <= p,
       binom(p+1,2)-binom(W+1,2) <= sigma,
       sigma = dW+binom(d+1,2)-Lambda.

   Thus p<=W+1 at length B(k). When sigma<W+1, including k=17, p=W
   and every middle target has one minimal witness contained in every
   other witness. Its witness family is a rectangle in endpoint
   coordinates. This does not assume a flat middle row. The separate
   total-middle-occurrence bound is W+2d+d^2. Root read the proof;
   bounded remote replay passed all stored exact words through k=16.
   The script is `verify_exact_b_critical_intervals_20260908.py`.

2. `EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md`
   proves a linear, rank-sensitive capacity bound at each entrance and
   exit of a coordinate. Every optimal k=17 word must have at least
   179 entrances AND 179 exits for every coordinate. The new bit must
   occupy exponentially many runs in any all-dimensional exact odd
   lift. This rules out bounded-piece or polynomial-piece lifts, not
   exact equality. Root and an independent agent checked the proof;
   the audit is `EXACT_B_ENTRANCE_EXIT_CAPACITY_INDEPENDENT_AUDIT_20260908.md`.

## New finite construction tool

`EXACT_PAIR_UNION_BINARY_HOST_COMPILER_20260908.md` gives a zero-added-letter
replacement theorem. For a supplied nonzero word E, install demanded
single-letter targets at individually legal positions, preserving DE.
With at most two supplied hosts per target, all simultaneous conflicts
are pair conflicts and the exact choice problem is 2-SAT. Every interval
of length at least two is preserved. Original one-letter-only targets
require explicit protection. Root read the proof; the independent audit
`EXACT_PAIR_UNION_BINARY_HOST_COMPILER_INDEPENDENT_AUDIT_20260908.md` passed.

This does not supply an optimum-length source, enough legal hosts, or
all-dimensional upper coverage. In particular it cannot repair missing
protected upper targets in the invalid k=17 OPT28 source.

## Earlier source-stage results, with the prefix now superseded

The following records concern the earlier source stage. Its geometry and
cut inventory remain useful, but the relaxed prefix is superseded above.

- `PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md` proves that all
  positive-three runs lie in exactly r-2 components of length 3(2r+1).
  At k=17 these are six 51-cycles and 306 owners. Root and two agents
  checked the algebra; bounded original-map checks ran on h100.
- `K17_PBBS_UPPER_CUT_CORES_AND_306_OWNER_SOURCE_STAGE_20260908.md`
  records the complete fixed k17 cut-core census and two exact finite
  path decisions. A literal 306-owner path now exists on the jointly
  safe cut bank, with three non-Johnson seams and valid depth-two
  replay. Its source has 308 nonempty letters. With the other 140
  cycles intact it retains every proper upper target. The global
  adjacent rank-eight palette has five holes; these are still obligations.
- Literal files: `badsix_relaxed_306_owner_path.word` and
  `badsix_relaxed_308_depth2_source.word`. They are source components,
  not universal words on 17 coordinates.
- The fixed census also shows that 59 original cycles lose an exclusive
  upper target at every cut, and opening every cycle loses at least
  129 distinct exclusive targets BEFORE new-seam witnesses. This is a
  recapture obligation, not a lower bound on nu(17).
- `PBBS_306_PREFIX_EXACT_DEADLINE_COMPILER_20260908.md` gives the
  one-pivot schedule, exact run tests and lower-cell atlas. Section 7
  accommodates the actual non-Johnson prefix. It still requires the
  remaining owner path, its upper coverage and one common lower compiler.

There is also a separate positive fusion route:
`EXACT_B_TAGGED_CONTEXT_FUSION_20260908.md` joins p>=3 cyclic components
with no added letters and preserves the exact OR multiset at EVERY old
width. Tagging the contexts removes the earlier repeated-owner obstruction.
An explicit k17 module fuses three 11-position cycles into one 33-position
cycle with 33 distinct rank-nine width-four owners. It preserves all old
targets and gains the full union. The arbitrary-p version gains the
cyclic hub arcs of sizes 3 through p. The full proof and example have an
independent audit. These permanent-hub components are not intact PBBS
components; a complete middle-layer partition into compatible modules and
a safe linear opening are not supplied.

Any proposed construction must simultaneously establish:

1. exactly one complete middle-owner chronology;
2. a valid physical deadline schedule and nonempty literal antecedent;
3. every required upper target in that same chronology;
4. a simultaneous lower-target compiler in those same physical cells;
5. length exactly B(k), with every join and boundary included.

Separate constructions of these properties do not compose automatically.
Even a successful k=17 instance would be a first case toward the goal,
not completion of the all-k objective. No equality theorem or new
optimal word is asserted by this checkpoint.

## Next actions

The latest height-adaptive result supersedes the older lane-specific list
below. All user-requested bounds and their completed proof/word audits are
now recorded in the master; no promised handoff edit remains pending.

1. Continue toward the exact equality goal using actual words. The best
   verified17word is24957, with644remaining positions aboveB17. A bounded
   next constructive step is to inspect the128 actual repair targets for
   a rank-decreasing pair-union forest, with no reused child, that emits
   fewer repair letters while keeping the24829prefix intact. This has not
   yet been attempted; do not claim any additional saving.
2. The general height-adaptive formula and thresholds are fully reviewed;
   do not restart the old logarithmic-rate constants or repeat the
   strict-height proof as an unresolved gate. Those routes do not give
   exact equality. Any further all-k advance must reduce the actual finite
   construction excess, not merely restate coefficient one.

The remaining items preserve earlier exact-prefix options as a separate
lane; they are not an instruction to abandon the new universal word.

1. Continue exact construction from the verified native291 prefix as a
   separate lane. Any B17-length completion has exactly24022 remaining
   positions and24022 missing targets at EACH of ranks8 and9. Since a
   position introduces at most one target of either fixed rank, every
   remaining position must introduce a fresh target at BOTH ranks. The
   rank potentials can therefore never increase during that continuation.
   Current b8=2,b9=3; a simultaneously middle-bearing state has
   b9=b8+1. Keep the actual word and all lower/upper targets together.
2. The arbitrary-endpoint full-width theorem is a further necessary
   check for that particular prefix: its rank-nine four-window block
   already begins at the first position. An optimal full completion must
   extend that same block to at least16909 four-windows (16912 letters).
   Thus at least16621 additional consecutive new rank-nine four-windows
   are needed before leaving the flat segment. This is an obligation,
   not a construction or proof of extendability.
3. Any proposed further fusion must be on genuine recurrent words with
   legal native states and disjoint new middle labels, as in the verified
   eight-cycle block. A complete static prefix cover alone is insufficient.
   The corrected sparseC6 and rank-potential proofs remain available, but
   the user's native alternating block is now the stronger concrete
   witness. Do not revive the full six-way biclique as an exact-bound route.
4. The original1513-sector PBBS construction remains an independent lane,
   with its existing facet and opening obligations. Its exhausted221-parent
   family cannot reach other sectors. The all-r upper-preservation theorem
   is already complete; do not repeat it as an open task.

All newly requested fixed-word and sharp-tail numerical checks have
completed. Root inspected the actual verifier, certificate and literal
artifact paths. No new mathematical job is currently awaited; revalidate
agent/process state before assuming any prior operation is running.

### Earlier lane-specific directions (retain only where not superseded)

1. For the concrete PBBS lane, continue from the NEW all-ports Johnson
   306-owner prefix. Do not restart the 17-safe-port bank or attempt a
   one-pivot completion of its old three-non-Johnson prefix. Account for
   the two new rank-eight holes and for every upper witness lost in the
   remaining cycle fusions. The existing one-pivot source theorem supplies
   the interface once the actual Q and common lower compiler are supplied.
2. For an all-dimensional construction, first investigate the symbolic
   all-r version of the new shallow bad-sector path. The separate tagged
   route must change its frozen adjacent-rank permissions; a complete
   fixed-hub middle partition followed only by deck-preserving fusion
   and capping is now excluded under the recorded flat-source hypotheses.
   Do not mistake the legal pulse cap for named lower-target completion.
3. Keep the lower compiler in the SAME actual source as all upper
   witnesses. The binary-host lemma is available only for its supplied
   domains; its cardinality and protected-singleton conditions must be
   checked before use. Scalar slack alone is not a solution.

All finite decisions reported above have completed; no remote computation
is being awaited. The all-r shallow-path proof and the tagged-module
protected-endpoint scope are now recorded and have root review. Inspect
live agent/process state rather than assuming an old run is still active.
The exact goal remains active; no all-k equality proof or new optimal
finite word has been established.
