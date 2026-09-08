# Exact equality research checkpoint

Date: 2026-09-09. Active objective: prove nu(k)=B(k) for every k>=0.
This checkpoint supersedes the active directions in the September8
checkpoint; that file remains the detailed historical record.

## Superseding current state: exact through22; main-branch publication requested

User supplied optimal21/22 words and then explicitly requested organization
of progress, the table, master handoff, solutions and asymptotic bounds on
main. This publication task is current; the all-k goal remains ACTIVE.
Do not restart21 as an unsettled finite case.

Both independent complete implementations PASS:
nu21=B21=352719;nu22=B22=705435;mu21=352716.
Nextunsettled23,targetB23=1352082;B24=2704159notattainedhere.
Raw21SHAeb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2;
raw22SHAa32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd.
Bothanswersfilesarecopied. Rootsuffix/range/cyclic/lift source
scripts/verify_k21_k22_optimal_suffix_and_lift.py,
SHAcf2701d2e7e3fe95d078d472a03caead671a20a671c34bacc160c73aece9fc1f.
One120CPU150wall3GiBh100runPASS13.289872s, all2097151/4194303witnesses
rangeORchecked;events4937949/9875974;maxsavedspan29notcutoff.
CoreC+C3verified,triples10/fours11bijections;everywitnessmodperiodvalid;
22periodicliftBYTEIDENTICAL. Completebundlewitnesses/k21_k22_optimal/,
reportSHAd5a6e51f5d5c14cf218b86c7e9ee1d8885f43525c87b1c58619e35d01e375706.
Independentforwardone60CPU90wall2GiBh100PASS7.739107s,
sourceSHAce205cef9f5f2208bcaccd1bb2f1d25ecd29f19f01782c17040ab89874080312,
events4937973/10228713. Completecopiedhashcheckedbundle
scratch/k21_k22_optimal_forward_20260909/;
reportSHA137029022789f1af18e949c870945a8b1d0bfb874b9e306f792b82770bdeb4fb.
AllrunsTERMINAL. The intermediate352862/705724pair passedrootfullchecks
withgaps143/289;itsforwardcheckerpreparedbutNEVERrun. Older375/753gaps
arehistorical. CurrentmainrecordK21_K22_OPTIMAL_AND_CYCLIC21_VERIFIED_20260909.md.

Positivepureprogresscompleted: two-orderconnectorletsall1430actual19ports
work (1371original/59swaps),onefixedh100runPASS andfullmixedbanksdisjoint.
Generalqbalancedpaddingadds2q−4coords,requiresparentresq,noamplification.
Twofurtherunused-sectorstepsandoptionalinjectivereentryproved, butrequires
additionalparentcutandtwo-stepagepredicate. NoteslinkedMaster9.38/Index.
Three-placementcompatibility/generalqobstruction/13vertexwithdrawalauditPASS
withcelloccupancy/minimalwitness/cyclicindexguards,linkedMaster9.39.

Publicationpreparation: currentbranchcodex/build-k17-llr-transfer-catalogue
atdfc1a927;mainisd2f26aa6intheCLEANworktree
/Users/amir.nuriyev/.codex/worktrees/coefficient-one-publish.RC4A2N/problem.
Branchesdiverged;maincontainsoldercoefficient-onepublicationpackagewhich
mustbepreserved. Fetchorigincompleted. User'snewmainrequestsupersedesold
snapshot-onlypublicationlimitforthisconsolidation. Do notforcepushorreset
anybranch. Preserveexistingdirtysourcework;stageexplicitreviewedartifacts.
READMEownedfrontierduringpublication;ASYMPTOTIC_BOUNDS.mdwritteninduction;
rootownsMASTER/RESEARCH_INDEX/currentexactrecordandGitintegration.

## Goal, authorization, and execution constraints

- The all-dimensional exact goal is ACTIVE and unproved. Do not mark it
  complete for an approximation bound, an isolated finite case, a valid
  conditional compiler, or an obstruction to one architecture.
- All mathematical execution/calculation is restricted to `ssh h100`,
  hostname `arboghast`. Local reading, editing, copying and Git housekeeping
  are allowed. Pure symbolic proof work is allowed.
- No broad/random searches. Every mathematical run must have one concrete
  bounded proof purpose, code read before execution, explicit limits and
  an honest result if capped. The user explicitly authorized committing
  the current research snapshot and pushing it to GitHub on2026-09-09;
  the earlier no-push restriction is superseded for that requested snapshot.
- Preserve the existing dirty worktree. Internal agent review is not
  human/external/formal certification.
- All runs reported below have exited and all artifacts have been copied.
  Check live agents/tools before assuming any old task is still running.

## Verified finite baseline

LATEST supplied bounds independently VERIFIED:
352719<=nu21<=353094, gap375;705435<=nu22<=706188,gap753.
Currentmain:K21_K22_CONTEXT_REFINEMENT_VERIFIED_20260909.md.
Raw21SHAf404c9f1e00bf40b24b1996ba31ee87c26cadfa70c2ca6140b04891685cb7392;
raw22SHAaef0f78939dec65f60ffffe3c1ce77999fdacdd3034964684884b7e5352d5a59.
Bothanswersfiles,completeforwardandsuffix/range/liftbundlesarecopiedand
hashchecked;detailsinNextusefulworkbelow. Full-cubechecksplusbyteidenticallift.

HISTORICAL earlier pair, also independently verified:
352719<=nu21<=353297, gap578;705435<=nu22<=706594,gap1159.
The separate357442/714884 report is WEAKER thanBOTHpairs.
Fullcubeforward+suffix+allrangequeriespass;22ordinaryliftbyteidentical.
Newmain:K21_K22_VERIFIED_UPPER_BOUNDS_AND_COMPILER_CONSTRAINTS_20260909.md.
21SHA0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7.
22SHA84e7448934c539fcc6c3453ffdb988cef219c263974ba49d876354fd24878b45.
Actualfilesanswers/k21_upper353297.word,answers/k22_upper706594.word.
Forwardbundle:scratch/k21_k22_upper_forward_20260909/;
sourceSHA80c2bbbf5e23b2fef51037b1273e00a4edb9a665de15dd3d8ef8a5399567300e;
reportSHA95a865796e3a2285f41a08d83657c411eefee334f428ff0c686c6e92f699b0ce.
Oneh10060CPU90wall2GiBpairedrun7.787seconds,fullartifacts copied.
Rootbundle:witnesses/k21_k22_upper/;
source scripts/verify_k21_k22_upper_suffix_and_lift.py,
sourceSHAa2bd77c798d1ea45955ddd32db1552e47df0b37f9bcbcc428bf41d8ebf8c46ec;
reportSHA13ff4356ddcb99d4200ae72a7c051e3e08459116d8275ff4b601643f072981a9.
Oneh100120CPU150wall3GiBpairedrun13.164seconds terminal0,allcopiedwith
remote/localhashcomparisons. Every2097151/4194303witnessrechecked;
suffixevents4943248/9886544,forward4943869/10241093;maxsavedsuffixspan24.

ThreegeneraltheoremsauditPASS, priorattributionretained:
scratch/SHORT_CELL_WEIGHTED_ORBIT_HALL_AND_PARITY_EXCESS_INDEPENDENT_AUDIT_20260909.md.
Capacity/scalingauditPASS underexplicitflatprotectedrankfloor:
scratch/WINDOW_RANK_DEFICIT_CAPACITY_AND_NEAR_DEADLINE_PROTECTION_AUDIT_20260909.md.
Exact21q2,t9pairdeficitsum>=401929−N;49210ONLYatN352719.
qprotected/d→1, gap≤(3k/2)^1/3;criticaloddg=O(k^1/6); claimedfinite
criticaldimensiontableNOTreplayed. Weaker357442literalnotattached.

The historical21structureand462Hallgraph reconstructions are COMPLETE,
bothsingleapprovedh100runsPASSwithcopiedandhashcheckedartifacts.
Actual3periods352548/105/63,+3each,then572repair. AllcanonicalPhi,
middle/envelope/rotationchecksPASS;569cyclicholes,579openedholes,
572tailrepairsall579. Candidategraph1997177edges,flow695397/demand695859,
Hall31185targets/30723cells givesEXACTdeficiency462. Fullproofs/reports:
scratch/K21_SUPPLIED_THREE_CYCLE_CARRIER_LOWER_HOLES_AND_572_REPAIR_CERTIFICATE_20260909.md;
scratch/K21_FIXED_THREE_CYCLE_PHYSICAL_CANDIDATE_HALL_DEFICIENCY_462_VERIFIED_20260909.md.
Neitherthisspecificgraphnor572tailisclaimedunchangedinnew353094literal.
Differentweaker12cycle357442skeletonMUSTNOTmixwiththis.
Do not rerun completedcertificates or start random/broadwordsearch.

The requested Git snapshot is COMPLETE: commit
dfc1a9270a4d681c6ef5975daae81810719a5c82 on
codex/build-k17-llr-transfer-catalogue was pushed to
git@github.com:anpaure/contiguous-or-research.git and the remote hash checked.
The work below occurred after that snapshot. No further push is authorized
merely by the completed snapshot request.

    nu(k)=B(k) through k=20.
    nu(17)=24313; nu(18)=48623; nu(19)=92381; nu(20)=184759.
    mu(19)=92378.
    First unsettled finite case: nu(21) ?= B(21)=352719.
    B(22)=705435 is a lower bound, not an attained value here.

Actual optimal words:

- answers/k17_optimal24313.word, SHA
  7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9.
- answers/k18_optimal48623.word, SHA
  6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5.
- answers/k19_optimal92381.word, SHA
  1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414.
- answers/k20_optimal184759.word, SHA
  047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02.

All four have independent complete coverage/witness checks and matching
endpoint lower proofs. Their constructors do not depend on PBBS
asymptotics. Do not restart searches for17–20 as unsettled cases.
The18word has been regenerated byte for byte from the17literal using
the endpoint689→8881 adjustment and the initialized reversed two-cycle
continuation. See the September8 checkpoint and main exact18 record.

The strongest conditional eventual rate remains
exp[-.93(k(log k)^2)^(1/5)] above k>=2^131073+1. Verified uniform finite
thresholds remain1%from29,0.1%from327,0.01%from1483,0.001%from6849.
These are construction bounds, not exact equality.

## Latest completed submission: exact19 and20

The user supplied actual19/20 literals. They are now independently
verified by two separate complete enumerations, with all saved witnesses
rechecked by a third range-OR implementation. No new search was run.

    k19: length92381, targets524287, missing0,
         forward1200848events, suffix1200846events, all524287rangequeries.
    k20: length184759, targets1048575, missing0,
         forward2494149events, suffix2401761events, all1048575rangequeries.

Both all-rank lower-bound calculations give equality. Exactlythree initial
endpoints lack rank10; all remaining endpoints give distinctten-sets.
Every saved ordinary witness has length at most29.

Let M92378,C=A19[:M]. The literal is C+C[:3]. All ordinary witnesses
reduce moduloM to valid cyclic witnesses, proving mu19=M by endpoint
capacity. AllM triple9/four10windows are bijections. Firstthreemasks are
364614,376898,104514. The20 word regenerates BYTEFORBYTE by

    A19+[524288]+[C[(3+j)%M]|524288 for j in range(M-1)].

Main record: K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md.
Forward source: scratch/verify_k19_k20_optimal_forward_first_occurrence_20260909.py.
Forward bundle: scratch/k19_k20_optimal_forward_20260909/.
Root source: scripts/verify_k19_k20_optimal_suffix_and_lift.py.
Root bundle: witnesses/k19_k20_optimal/.
Root report: complete_suffix_range_cyclic_lift_certificate.json.
Root sourceSHA9c416217353518fc7ea94efbf716205fdcbdb68c30dcb21b902fd2353859fafe.
Both sources fully reviewed before one h100 run each,60CPU90wall limits.
Forward~1.805seconds; root~3.226seconds. No partial run treated asPASS.

Separate actual19 structural reconstruction PASSED: canonicalPhi fixed
on ALL92378outgoingedges; incomingchanges70452, unchanged21926.
Native360components becomeonecycle. Envelopesrank7; nativepairrank8;
actualcaps change12654pairs while preservingtriples9/fours10. All169765
targets ofrank<=8 occur inactualletters/pairs. Pair-onlyrank<=7total11324.
All4862rotation-quotientrows INCLUDINGcaps are equivariant and recovered.
This is literal reconstruction, NOT a replay of the unprovided compact
generator or search. Artifacts linked in the main record.
Full structure bundle: scratch/k19_literal_structure_20260909/.
ReportSHA68c2187cd9ec3d7ccf14c35588265e32fb96daacafe48e63d1325b3f2e02c566.
SourceSHA4db31c92fd839768205d10a1e0a2168a9a7520215e466b4aca0537ea125627d7.
Single60CPU90wall2GiBh100run finished2.659seconds; allartifacts copied
and hash-checked. Note:
scratch/K19_OPTIMAL_LITERAL_PHI_CARRIER_PAIR_CHANGING_COMPILER_AND_QUOTIENT_CERTIFICATE_20260909.md.

The general periodic-corelift and endpoint/set-turnover laws pass pure
proof review; see scratch/K19_K20_ENDPOINT_PERIODIC_LIFT_AND_TURNOVER_AUDIT_20260909.md.
At21 the prior paired-endpoint theorem requires16793 exits ANDentrances
percoordinate, strongerthanuser5599. At19 it required4859, notonly1621.
Do not misstate either as an impossibility result.

The new spectral nativebarrier audit is
scratch/PBBS_BOUNDED_HEIGHT_SPECTRAL_CONSTRUCTOR_BARRIER_INDEPENDENT_AUDIT_20260909.md.
It proves Cnative>=1+3ceil(2^r/(r+1)-1) and a stronger averaged lower
penalty (3pi^(2/3)/2+o1)(n(logn)^2)^(1/3). The conclusion
Nnative−B=2^(n−o(n)) was already known at a weaker penalty. It is NOT
a lower bound on unrestrictednu and does not contradictoptimal17–20.

Next proof direction: construct suitable fixed-Phi recurrent cores with
residence, all-rank coverage, simultaneous short-windowcaps and safe
opening in every odd dimension. Successful17 AND19 now fixPhi, but no
general existence/safe small-flipfactorization is established. The even
periodiclift is general only once those hypotheses are supplied.

Final pure capacity audit, read byroot:
scratch/UNIFORM_CYCLIC_MIDDLE_WINDOW_CAPACITY_AND_OPENING_OBSTRUCTION_20260909.md.
If a cyclic universal width-M core has allq-windowsrankr atn2r+1,
q-window and(q+1)-window rows MUST be middle-layerbijections. Alllower
targets use<qpositions, giving qM>=4^r−1. A universal periodicprefix
opening needsd>=q. Therefore requiredq isOmega(sqrt r); fixedq3cannot
be the all-dimensional construction. At d=q lower/middlewitnessesall
survive, but higher safe-opening remainsseparate. This is an existing
endpoint-capacity specialization, NOT a newgenerallowerbound or new
numericthreshold. No computation ran.

Other pure proof work completed during this continuation, retained for
the next all-k step rather than a new19search:

- scratch/PBBS_PHI_LEXICAL_MATCHING_AND_PUBLISHED_HAMILTON_RESIDENCE_AUDIT_20260909.md:
  Phi is the standard lexical matching. The specific book-proof pull
  family fails the first residence exclusion for every allowed spanning
  tree; nine-vertex stencil disjointness prevents other pulls repairing
  its isolated coordinate run. This does NOT exclude all Phi-containing
  Hamilton cycles (actual17/19 are counterexamples to such a broad claim).
- scratch/EXACT_TWO_PROJECTION_CURSOR_GLUING_AND_COMPOSABLE_RUN_CREDIT_20260909.md:
  exact local compatibility of two projected tag cursors and composable
  paid run-credit ledger; no global simultaneous assignment claimed.
- scratch/K19_DISJOINT_OR_BUNDLES_AND_COUPLED_INTEGRAL_HOST_HALL_20260909.md:
  whole-bundle Hall condition avoids false independent-channel credit;
  a conditional host theorem, not an executed allocation or all-k proof.

## Earlier user submission: moment-prefix uniform10ppm from137

Supplied files were read completely and preserved:

- scratch/MOMENT_PREFIX_ADVANCE_USER_PROOF_20260909.md
- scratch/MOMENT_PREFIX_USER_VERIFICATION_LOG_20260909.txt

Only proof and log were attached. No3356-case transcripts, generator,
audit program, archive or predecessor lower certificate is available.
A text question asking the local package path remains pending. The
earlier713-case57/87prefix package is also still missing. Do not treat
the absence of these files as a block on the all-k exact research.

The new mathematical method PASSES internal proof review:

    K(a,b)=binom(a,b)binom(a,b+1)/a,
    H(a,0)=1,
    H(a,b)=K(a,b)+sum_c binom(a+c,2b)H(b,c).

Prefix charge: w[(2s−1)K+2H]/P. Exact row integration uses
P_d=lcm(P,den(beta'/d)), P|P_d|P_p and the nonnegative proper-period
correction. Arbitrary-subfamily reflection bound, sparse exact-mass
reserves and final integer normalization are sound. Guard terminalb0,
t>=a in the reflection heuristic, and exact/downward predecessor sums.

Root read both proof audits and the entire new independent checker;
structure independently read the code before execution. A SINGLE r68
case and structural audit ran onh100,60CPU90wall1GiB,1.5324seconds:

    Cat68=86218923998960285726185640663701108500
    U=860872256709126171307785011672491
    Cat68−100000U=131698328047668595407139496452008500>0
    U/Cat68<0.000009984725125072396316850761.

All162refinements/2571nodes/2409leaves are completely replayed, with
2388unfinishedleaves, maximumdepth3. Exact H through100 and exact
row-period classes throughout; no sparse reserve or approximate symmetry
correction needed in this instance. Structural checks:23713Dyck roots,
125475middlebridges,2575orderedrows,288smallprefixstates. H10050/K is
16.428245020843044252579122292728… versus oldcap51.

This proves137/138ONLY. It does not replay the other3355cases, the
predecessor135/136failure, or uniform137. The inherited decreasing
envelope already covers r>=3424 once a complete finite band is supplied.

Mainrecord: HEIGHT_ADAPTIVE_MOMENT_PREFIX_CERTIFICATE_METHOD_20260909.md.
Numericalnote: scratch/MOMENT_PREFIX_R68_INDEPENDENT_NUMERICAL_CERTIFICATE_20260909.md.
Code: scratch/verify_moment_prefix_structure_and_r68_20260909.py.
Fullbundle: scratch/moment_prefix_structural_and_r68_20260909/.
ReportSHA4a72d1ed42e689b59eff6e7b80bf082e5cc7044b436731a18313834794df16d4.
SourceSHA6f1f556319147121250420d4715a21e0a7cbf3a679392b3b7b8b210a11c17132.

## Exact-goal progress completed in this continuation

Mainrecord: EXACT_EQUALITY_FIXED_MATCHING_AND_RUN_CONSTRAINTS_20260909.md.

### Fixed canonical matching in the actual optimal17 carrier

The actual85/24225cycles recover all24310lower/upper incidences and
1430rotation-quotient rows. Its outgoing matching equals the canonical
PBBSmatching on EVERY lowerlabel; incomingmatching changes17578labels.
Relative matching cycles:289oflength3,68oflength5,oneeach34,170,16167.
The giant length16167is one circuit; quotientgiant951. Safe small-flip
factorization is NOT known. Actual two-step residence violations0 versus
native119(allheight2). The full literal comparison ran once,0.530seconds,
30CPU45wall1GiB, before the user moment continuation; root read allcode.

Proof:scratch/K17_OPTIMAL_CARRIER_FIXED_PBBS_MATCHING_AND_EXACT_DIFFERENCE_CERTIFICATE_20260909.md.
Bundle:scratch/k17_optimal_carrier_comparison_20260909/.
This is actual membership in a fixed-matching family, not all-k existence.

### Complete insertion obstruction for the actual18 trace

The word has maximum letterrank7. Every48620nine-set has a unique
endpoint; first threeendpoints lackone. The firstnine-set76467 endsat3
withgreatestwitnessstart0. All48622internalgaps have a fatal shortest
old-nine-set witness. Therefore a19superword with THIS EXACTunmarked
subsequence can only add markedletters before/after the contiguous word.
One root-authored/source-reviewed h100run0.27274seconds,30CPU45wall1GiB.

Proof:scratch/EXACT_INTERLEAVED_LIFT_RUN_START_BUDGET_AND_FIXED_TRACE_CUT_CORES_20260909.md.
Bundle:scratch/k18_fixed_trace_cut_cores_20260909/.
Earlier fixedK16 occupied-cut theory is prior; this complete18instance
is new. Reversal/relabeling preserve the obstruction.

### New paired-endpoint theorem and stronger finite conditions

For ANY partial word lengthN and distinguishedz, let a_s be the number
of old rank-s targets and b_s marked rank-(s+1)targets represented:

    a_s+b_s <= N+R_exit and <=N+R_entrance.

Choose one endpoint per target in each family. Shared endpoints force
targetsD,D+z and cumulative unmarked-run prefix exactlyD. A run has at
mostone distinct rank-s prefix. Hence shared endpoints inject into runs.
Reversal gives entrances. For universal oddN=W(2r+1)+d:

    R_exit,R_entrance >=max(0,Cat_r−d).

At17thisis1427; at19it is4859, superseding541. The old ledger already
contained the deficit numbers and endpoint-overlap step, not this
run-injection conclusion. Proof independent of PBBS.

WithM unmarkedletters and H_s rank-s unmarked-run starts, combine
R_total−H_s<=M−W_s to getH_s>=max(0,3W_s−N−M), alsoforends.
At exact19,M48623:4856literalnine-set starts/ends (supersedes4835).
Withno rank9unmarkedliteral: M>=53479,4856extra(supersedes605).
Atmostoneexitfixedtrace: N>=97239(supersedes97234). None is a lower
bound excluding unrestrictednu19=B19.

One reviewed diagnostic ran3.6019seconds,30CPU45wall1GiB:137256small
words throughlength6,bothorientations,1647072familychecks,227130shared
events,454260literalwitnessreplays. Actual17/18runstatistics only were
checked withhashes; fullcube was NOT reverified. Actual17exits/entrances
2231–2232; actual18newcoordinate0exits/1entrance.

Proof:scratch/PAIRED_ENDPOINT_CATALAN_RUN_BOUND_INDEPENDENT_AUDIT_20260909.md.
Code:scratch/verify_paired_endpoint_run_theorem_and_exact_literals_20260909.py.
Bundle:scratch/paired_endpoint_run_diagnostic_20260909/.
ReportSHA2fdc338e54cff94664ffd07058eb7714fc8aa8f2e8bd424b497b7af930da3a67.
SourceSHAba675de0908439ff68aa8da3ae9dd9ad7a5061beec900ac41f24a46f753c3f37.

### General conditional compilers, no executed solver

scratch/EXACT_MANY_RUN_RECENCY_CURSOR_AND_PROTECTED_WITNESS_COMPILER_20260909.md:
afterlasttagq, B=oldunionafterq,C=Bunionoldprojectionatq. Oldprefixes
lieinB; markedprefixescontainC; dualD/D+zrequiresB=C=D. Exacttagging
compiler choosesoneprotectedoldintervaleachD, unionF; allforcedtags
andallzeroprojectionpositionsavoidF; everyD'stotalwitnesspositionunion
H_DhasapositionoutsideF. MarkcomplementF. Atleastonezeroprojection
positionneededforthe singletonnewcoordinate. Coupledchoicesunprovedallk.

scratch/K19_GENUINE_PAIR_RESERVATION_LEMMA_AND_NEXT_FINITE_GATE_20260909.md:
exactproper-subletter menu, independenttriple-preservingframe and
target/block/displacedrank8label integralreservationflow. Noexecution.
Important correction: rawq counts locallyproperpairs, notnetglobally
nonliteral targets. WithfrozenH3positionsF,distinctliteralsL_F,reservedT,
residualliteralcapacityrequires|T−L_F|>=6669+|F|−|L_F|. Rank8/upper
preservationalone doesnotpreserve displacedrank7orallsmalltargets.

scratch/K19_PAIR_RESERVATIONS_COUPLED_BACKBONE_HALL_CONDITION_20260909.md:
DEFER standaloneqflow. A meaningful coupledcertificate must choose
one retainedrank8witness perunprotectedlabel, put explicitcoordinate
backbonesonit, andsaturateALLresidual lowtargetsbyaneligiblefree-position
matching. Backbones⊆target⊆sourceletter preservesallchosenrank8witnesses
andtheanchoredtripledecksimultaneously. Choiceofreservations/backbones
notprovided. Evenpassingwouldfirstgivecyclicbank;fusion/openingseparate.

## Do not repeat completed or inadequate gates

- Do not treat19 or20 as open: their complete supplied optimum words
  are verified above. Earlier19-specific model gates remain historical
  architecture analyses, not unfinished tasks needed to settle19.
- No fixedtrace18 interleaving or one/two-seam19search: nowexcludedabove.
- No rawq≥6669flow promoted to full lower allocation; use the coupled
  witness/backbone/Hall interface or defer execution.
- No rerouting unchangednative/full-D recencyinventory: completeDAG
  obstruction already established at17. The successful17word changes
  incomingmatching andliteralinventory.
- No fixednative17unrestrictedH3caps decision rerun: independentDRAT
  UNSATalreadyestablished for that chronology. Newoptimum changesit.
- Staticwhole-rank/partialrank7normal-chainization has extensive prior
  results. At19the H3whole-rankcapacityshortfall andpartialrank7split
  normality are ALREADYknown; chronology/commonallocationremainopen.
- Do not replace all-k exact goal by sharperperiodasymptotics. The native
  constructor's actual additivecollar is exponential; changingitsword
  orstateassignmentisnecessaryfor exactB.

## Next useful work

CURRENTTURN classifiedPROGRESS: newrawsuppliedwords VERIFIED independently,
newpositiveprivate-head/ageinterface proved. All-kgoalACTIVE,noblocker.
One bounded PURE task remains running with exact_equality_structure:
derive correctedconnectorbank fromembeddedinnerfactor00X11 on2r−1active
coordinates, creditexistingbalancedDyckembedding. Noexecutionauthorized.
AtrootX0D, replaceedgeby000D11→001D10→011D00→1110R00,D1R.
Conditionalactualinnerres3historysuppliesa,bpermanent; notknownat17
merelyfromoptimal17word. RootledgerM'=C(2r−1,r−1),h'=Cat_(r−1):
usedlowerM'+3h', consumeduppers/assignededgesM'+2h', h'openpathsplus
root-freeinnercycles. Starts00σ_inner(0D)11,ends1110R00. Newbanks10/00
disjointinternally; clashesouterparent10/oldq3second11notresolved.
Agentaskedtofinishonlythisboundednote,notexpandintosolve/search.
Revalidateitsstatus/readresultnextturn;donotlaunchduplicate. Allmathematical
verificationprocessesareterminal;onlythispureproofagentwasliveatcheckpoint.
LATESTBEST:352719<=nu21<=353094(gap375),705435<=nu22<=706188(gap753).
answers/k21_upper353094.word SHA
f404c9f1e00bf40b24b1996ba31ee87c26cadfa70c2ca6140b04891685cb7392;
answers/k22_upper706188.word SHA
aef0f78939dec65f60ffffe3c1ce77999fdacdd3034964684884b7e5352d5a59.
Root+inductionfullreadsourceBEFOREone120CPU150wall3GiBh100suffix/range/lift
runPASS13.290546s,src197d30ce52b14f085fbf1ba457da11b614afbf7485ccaf4538b86154a55b740a.
All2097151/4194303witnessesrangeORchecked; suffixevents4943001/9886049;
maxsavedspan24both,notcutoff.22byteidenticalordinary2Nlift.
Bundlewitnesses/k21_k22_context_refinement/,reportSHA
1e01464fd535dd1d20edc850e07d2b83406fcd460830accc56a7afab8714fddf.
Remote/local5principalhashesmatch,exactcommand/provenance/logsaved.
Indepforwardone60CPU90wall2GiBh100PASS7.690287s,events4943081/10239314;
source13908957a5df1afed72a1af1283eefd15b242252251f9cc04aabde88691acba1.
Bundle scratch/k21_k22_context_refinement_forward_20260909/ allcopied+SHAchecked,
reportSHA1a2feac92dd112ce89dd31a1d2654af10ef04d5f86603d74b32e659604bcb875.
Everytarget/rankandBcomputed, noperfectoptimumclaim. Earlier353297/706594
historical; weaker357442notincumbent. No644trace/202scheduleprovided/replayed.
Main K21_K22_CONTEXT_REFINEMENT_VERIFIED_20260909.md,answers/README,
finitecomparison,Master9.36/Indexupdated. No push. Noprocessremains.

NEWPUREPOSITIVEreplacement (rootfullread,frontier/inductionPASS):
scratch/Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md.
U011D00 everyres2historyforcesx,yagesEXACT1,2; allDones≥3.
S_z=U+z−x; previousinversealwaysdeletesy exceptz=b,w=u whichcloses1-run.
Thus110DdeletionINVALIDres3, validmenuonlyD-one deletions. D=1R choose1110R,
injective/privateheads. scratch/FORCED_111_D_FREED_HEAD_MENUS_AND_PRIVATE_DYCK_BANKS_20260909.md
hasfullforward/inversemenu, privateheadtypes1101R/1110R;agegateselectssecond.
Conditionalconnector000D11→001D10→011D00→1110R00 needsinitialb≥3,a≥2.
Actualinputhistories/globalunuseduppermatching/onecycle/coverageNOTproved.

NEWGENERALqageinterface(rootfullreadandbothpeersPASS):
scratch/CANONICAL_PHI_BACKWARD_AGE_OBLIGATIONS_AND_INITIAL_PLATEAU_THEOREM_20260909.md.
Rootappliedminorfrontierguards≥1toinitialgraphsetup. InQj=0^j1^(j+1)D00,
validresqhistorywithmin(q,j+1)incomingedgesforcesplateauages1..m,others≥m+1.
Suffix-minlemma(inverseatorbeforefirstnamedoneexceptfinalbwhenm1) plus
short-born/closed-runexclusionsprovesinduction. Ifj+1≥q−1 exactmenu.
j=q−2,D1R,q≥3:0^(q−2)1^(q−1)D00→0^(q−3)1^q0R00 injectiveage-safeedge.
NestedRbackwards: requireR1subsetP; R'_t=R_(t+1)∪{forwarddeletedbit};
trueboundaryagesmustdischargeobligations. ExactfinitewalktestNOTfullfactor.
Audit scratch/CANONICAL_PHI_PLATEAU_AGE_THEOREM_INDEPENDENT_AUDIT_20260909.md.
Master9.37/mainq3recordupdated. Nextpositivework:integratecorrectedselective
headbankandactual11inputagehistorieswithoutfixedinventorycollisions;
support/compiler/openingremainseparate, cannotjustreopenalloldrootentrances.

Useroverlappingrefinementtheorem purePASS:
scratch/ORDERED_OVERLAPPING_REFINEMENT_AND_SIMULTANEOUS_CONTEXT_CERTIFICATES_AUDIT_20260909.md.
Orderedoverlappingintervalrepresentations preserveALLoldsubintervalOR;
fullreplacementboundariesrequired. Disjointoriginalblocks+guardedinsertion
gapseditscommute,preserveallORinarbitrarycontext; focalrepairfirstproof
showsalllocalcertificatecontextscoexist. PairfactorisMASTER3.2depth1.
Exact21transportedrank11witnesscap4stillnecessary;inflationto5can'tbe
ignoredbychoosinganotherwitness. Doesnotrefuteunrestrictedrefinement/nu21.

DECISIVE NEW PURE OBSTRUCTION (rootfullread+induction+structurePASS):
scratch/Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md.
ForD Dyck(r−1), child00U=011D, outgoingupperZ=111D. Every nonself
arrivalatU insertsoldsecondbitx: everyupperU+z,z≠oldfirstu, haslastmin
−1atoldfirstposition, whoseinversePhi deletesx; z=u givesforbiddenself.
Z'sotherfacets areV=101D (deletesfreshx), orstrictlypositive1D'heads.
Allthese1D'headsoccupiedbyFIRSTrootentrances L+a→Phi(L)00. Therefore
retainingALLfirstentrancesforcespositive1-run, forbiddinganystrictfull
residence>=2factor. Independentofparentcopy, Hallchoices, whole01strip.
Stronger: allCat_(r−1)Z needDISTINCTfreed1D'heads, henceatleastCat_(r−1)
ofCat_r prescribedfirstincidencesmustchange; ratio(r+1)/(2(2r−1))→1/4.
Localdisjointbanktheoremstilltrue, butWHOLESALECOMPLETIONIMPOSSIBLE.
Do not keep treating unused-sector matching as sufficient nextgate.
Next: selective/replacedports respectingforced-headmatching andages;
allrankcoverage/compiler/openingstillseparate. All-kgoalACTIVE.

Additionalrootfullreadpuretheorem:
scratch/SMALL_FAMILY_SHADOW_HALL_WITH_FORBIDDEN_FACETS_LIMITATION_20260909.md.
k=r−1,fixedcoreZsizet, Vsize2(k−t), familyZ∪binom(V,k−t), forbid
removingZ. NeighborhoodsmallerbyCat_(k−t). t=ceil(log4(2(r+1)))−1
givessize≤Cat_r forr≥7. ThusO(logr)arbitraryforbiddenfacetscanbreak
theCatalan-sizeHallargument. NOTrealizedactualparentages/prefixfamily.
Valid sufficientrobustbound |F|≤binom(k−1+k/(t+1),k) alsoproved.
No newexecution;donotclaimallkno-gofromabstractagecounterexample.

LATEST completed fixed21 reconstruction: both approved single h100 runs
PASS, no process remains. Root read both full reports and proofs.
- scratch/K21_SUPPLIED_THREE_CYCLE_CARRIER_LOWER_HOLES_AND_572_REPAIR_CERTIFICATE_20260909.md:
  periods352548/105/63, allPhi/middle/residence/envelopechecks,569cyclicholes,
  tenopeninglosses,572distinctrepairletterscoverall579prefixholes with
  independentrangequeries;capsnotrotationequivariant6520violations.
  Bundle scratch/k21_literal_structure_20260909/, reportSHA
  7b2230f8a92fc6e7d8498d7dd632ca3dda0a6418894d0084dcc19b677887c829.
  One60CPU90wall2GiBh100run8.926s, fullartifacts/hashes copied.
- scratch/K21_FIXED_THREE_CYCLE_PHYSICAL_CANDIDATE_HALL_DEFICIENCY_462_VERIFIED_20260909.md:
  graph1997177edges, flow695397/demand695859, EXACTdeficiency462.
  FullHallset1485orbits/31185targets, neighborhood1463orbits/30723cells.
  33243positiveflowrecordsreplayed;all2011584localmasksregenerated.
  Bundle scratch/k21_fixed_candidate_hall_20260909/, reportSHA
  149c4e9a88ab9f88e66cac1fe8ebed0cc0f79078a3dcbea3d8e37d00d69132a9.
  One reviewedC++build60CPU90wall2GiB, one120CPU150wall2GiB run2.879s.
  Rawinput/fullgraph/primal/dual/physicalsets/binary/source/commands/logs
  allcopied+hashverified. DeficiencydoesNOTboundrepairpositions ornu21.
Strong21/22incumbentsunchanged. Mainnote/Master9.34/Indexupdated. No push.

Currentturnpuregluingprogress (rootreadallthreefullproofs):
1)scratch/Q3_EXCURSION_EXIT_AGE_TEST_AND_EXACT_OUTPUT_ENCODING_20260909.md:
outputTminEXACT−3, freshαage2,βage1. Followingparentisiffd(T)avoidsboth
andd(σT)avoidsβ. ExactDyckreturnsaftermax(d,e), inverseoutputencoding.
UnfilteredHallcannotautomaticallywithstandtheseexclusions.
2)scratch/Q3_EXCURSION_PARENT_COPY_DEGREE_DEFICITS_AND_DIRECT_SPLICE_OBSTRUCTION_20260909.md:
Irootports,P=σI,Toutputs,H=σ^-1T. 2Catcutsmandatory,HdisjointI,P.
Directparent10spliceneverHamilton: mouthHwithoutu hasnoheadP;
ifallHcontainu thenHALLu-deletiontails, cutsalternate,graftsclosecomponents.
Residualgraphandexplicitfree00mouthsuccessorsproved; extraedgecuts/sector
routingrequired. Notallkno-go.
3)scratch/COMPLETE_CANONICAL_PHI_SECTOR_LAW_AND_EXPLICIT_01_STRIP_EXTENSION_20260909.md:
completePhi6blocklawoldprefixB/F,G+/G−, J/J+bijections. Naturalincoming
upper01 givesentire01firstreturnstrippathcover;fixedrootunitpathsare
alreadyinbank,allotherscanbeaddedwithoutcollision. ForHamiltonparent
thereareCat_(r+1)paths,usedlowerM+Cat_(r+1)+4Cat_r,upperM+4Cat_r.
Explicitremaining3bandgraphcounts, notmatching/age/topology/coverageproof.
Master9.34–9.35andmainq3recordupdated. All-kgoalACTIVE.

### Latest exact-goal continuation after the requested push

Root's full record is EXACT_PHI_INDUCTION_AND_UPPER_SUPPORT_GATE_20260909.md.
Master9.33 and the latest RESEARCH_INDEX entry now record this direction.

The canonical-Phi local excursion is PROVED for q>=2,r>=q+2, legitimate
input age history and a fixed-root port0D with added10. It hasq+2steps,
one00,one01,q−1 distinct11states, and b-run exactlyq lower/q+1upper.
Parent-following entrances00=Phi(L),01=sigma(L) are injective when the
child age history agrees with/dominates the parent's. First11 is
sigma(L) intersect sigma²(L). Exit J(K)=K+firstmin(K) is injective;
invert by deleting the up-step after the LAST minimum. Its image is the
old rank-r minimum<=−2 class. Distinct terminal11 states give distinct
exits, all disjoint from fixed-root entrances because u is protected.
Independent internal pure-proof reviews pass with the explicit age
hypothesis. Global11 allocation/age joins/upper support/compilation remain.
Note:scratch/CANONICAL_PHI_BALANCED_BLOCK_BARRIER_AND_MINIMAL_RUN_SECTOR_EXCURSION_20260909.md.

VERIFIED counterexample: Phi+Hamilton+residence does NOT imply first-higher
upper support. Reorder actual19 lower R as
R[:7898]+R[53069:78118]+R[7898:53069]+R[78118:]. All middle labels/Phi/
Hamilton/residence remain, but target109931rank11 is absent from ALL upper
intervals: its eleven upper subsets are isolated. Nonempty source exists;
caps preservingfour-window owners cannotrepair it. Three incomingchanges
are minimal nontrivial matchingdifference (noC4). Not an obstructiontonu19.
Fixed1216threecircuits:494Hamilton,969resident,361both,19counterexamples.
Firstfullreplay passed. h100one60CPU90wall2GiBrun0.744seconds, allcopied.
SourceSHA5b11d71a35ca70695daea0db915224f79e1c1e3053efd6ef7e4d2b720e449702.
Proof:scratch/PHI_HAMILTON_RESIDENCE_DOES_NOT_FORCE_FIRST_UPPER_COVERAGE_20260909.md.
Bundle:scratch/k19_phi_upper_three_circuit_diagnostic_20260909/.

Fixed19 opening proof reduces onlytheSUPPLIEDcut to255 propertargets
containingV=Ulast unionU0. Completecompatible runs and coordinate first/
lastextrema give the exact criterion. This credits oldwitness-coretheory,
notnewautomaticopening. Source fullyroot/frontierreviewed; onefixedphase
h100run60CPU90wall2GiB completedPASS4.023seconds,noothercuts/edit/search.
All255targets pass:229crossingrunsincomplete,25othercompleterun,
1uniquecompleteleftwitness. UniqueT515158rank12 usesfinal6sourceletters
[92375,92381)zero-based. All20827minimalownerwitnesses enumerated,
20807retained;436900compatibleruns,12840complete. Everytargetoneowner/
sourcewitnessreplayed. Rootreadactualreport.
Bundle:scratch/k19_fixed_cut_255_20260909/.
SourceSHAac22b980ff3f3b1d079324159e8d1a0acc3514ec3265f568474a4cd87ca11af6.
UniqueT515158solecompleteownerrun[92375,92378]inclusive hasminimal
witnesses[92375,92377],[92376,92378],f92377,l92376. Forcededgecore
isentering92377only. Pureconsequence: openingatphase92377(oneback)
wouldloseT. Noadditionalcutrun/search. Thusalreadyuniversal19isNOT
safeateveryphase. Thisdoesnotdenyexistenceoforiginalsafecutphase0.
Proof:scratch/EXACT_OPENING_COMPLETION_RUNS_PRINCIPAL_FILTER_AND_FIXED19_DIAGNOSTIC_20260909.md.
Source:scratch/inspect_k19_single_supplied_cut_255_upper_targets_20260909.py.

Actual19 fixed-root facet diagnostic COMPLETE:4862 bit0-rootports, all
threeprescribedPhi21entrancesteps andliteralparentagespass. 00/01each
4862distinct;first11has4487images=4112singletons+375collisionpairs,
750collidingports,excess375,maxmultiplicity2. Exampleports3763,42017
shareoldfacet4511/child11state1577375. One30CPU45wall1GiBh100run
0.337seconds; fullroot/frontier/structuresourcereviewsbeforeexecution,
allartifacts copied. Noalternativechoiceorsearch. Rootreadactualreport.
Proof:scratch/K19_FIXED_ROOT_PRESCRIBED_PARENT_SECTOR_PORT_CERTIFICATE_20260909.md.
Bundle:scratch/k19_fixed_root_parent_sector_ports_20260909/.
SourceSHAc8bdcd0161aaa3f7ce676636223de8f37f1d8b3f4fb72afa0ad0c42dfe7f832e.
ThisexcludesusingALLprescribedfirstentrances, not21existence.

New PURE repair PROVED, root/induction/frontierindependentreviewsPASS:
atq3alloldseconddeletions
e∈L−d haveaged3bythirdstep. Small-familyKK+Hall choosesdistinctfirstK
forALLCat_rports whenr>=7; priorKKmachineryreused, notnewshadowtheorem.
Then deleteu inONEinternal11step: uage3legal, K'=J(K)−u. InjectiveJ
andcontainmentofu makeK'distinctanddisjointfirstK(allcontainu). Final
outputJ(K')injectivewithmin<=−2, disjointinput0D(min−1). Thiscloses
thewholeq3five-stepbankallocation. The resultingCat_r paths arepairwise
vertexdisjointincludingall6banksandupperowners. Atactual19thereare4862.
Bothuandblowerpositive runsareexact3, aexitage3. No spanning/gluing/
targetclaim andno matchingconstructionrun. Outputs maycoincidewith
untouchedparent10states; thisisthenextglobalcompletiongate.
Audit:scratch/Q3_FIRST11_COLLISION_REPAIR_BY_SMALL_SHADOW_HALL_INDEPENDENT_AUDIT_20260909.md.
PriorKKHallsource:MATH_THEOREM_CATALAN_CAP_TWO_COMPRESSION_20260731.md§1,
MATH_ATTACK_N_FULL_ORBIT_ESCAPE_AND_Q1_CYCLE_20260725.mdLemma5.1.
Primaryshadowstatementcheckedathttps://arxiv.org/pdf/0806.2023p1.

Uniform exact-width middle-window rigidity/qcapacity alreadyappears in
Master3.40; the scratchcapacitynote nowcorrects attribution. q mustgrow;
d>=q applies ONLYto literalprefixopenings, notgenericblockrepair.
Do not rerun fixed17–20 search or invoke oldnativeperiodestimates as an
additive route. The finite frontier remains21; all-kgoalACTIVE.

If the user supplies the moment/earlierprefix package, inspect source
before one explicitlybounded transcript replay; promoteonlythecases
actuallychecked. Do notinferall3356fromthefirstpair. Existing analytic
tail is alreadyproved anddoesnotneedrerunning.

For exact equality from21 onward, use both actual fixed-canonical
matching successes at17 and19 and
the strongerpairedrun constraints to specify a genuinelynew chronology
or a fullycoupled lowercompiler. The simple protected-witness tag model
and witness-backbone Hall theorem are exact finite interfaces; existence
of jointlysuitabledata is the livegate. Neither an arbitrary middle-level
Hamiltoncycle nor a staticchaincover suppliesallthoseproperties.

No newly discovered word is claimed: the supplied19/20 words were
independently verified and their19core/20lift reconstructed. All-k
equality remains ACTIVE. Master9.29–9.32, the exact19/20 record,
finite comparison, answers index and RESEARCH_INDEX are updated. Earlier
details andproofs remain in scratch/EXACT_B_GOAL_CHECKPOINT_20260908.md.
