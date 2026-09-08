# Bank-wide parity coupling with an exact distinct-target ledger

2026-09-07. Pure finite proof; no computation. Full independent audit and
a separate score/stationarity audit passed. The fixed-weight and gauge
qualifications below incorporate their requested clarifications.

This extends the two-chain fair-cut coupling in
`/Users/amir.nuriyev/.codex/worktrees/7796/problem/research_round1/TWO_CHAIN_NET_COVARIANCE_COUPLING.md`
to simultaneous changes of many chains. Chains need not be paired off:
one chain can interact with several others through disjoint physical
block vertices. The conclusion is NET actual coverage, not preservation
of every old target. Multiple interactions affecting the same target are
accounted for exactly rather than counted as separate gains.

## 1. Finite actual-support model

Fix a finite set of targets with nonnegative weights w_T and a bank of
legal chain words. All word lengths and any exterior word stay fixed.
Assume its actual support is exactly the union of the individual chain
supports and the fixed exterior. Full-universe guards and the audited
purity-band compiler provide this hypothesis for the common-root chains.
Outside that band either include an exact support model or use a fully
paid fixed repair; unnamed incidental witnesses must not be ignored.

In chain m, index independent fair cut signs by a finite vertex set V_m.
One may fix disjoint global label pairs and partition the cells for each
pair into move blocks. Toggling a pair in a block gives a legal phase
system. Distinct label pairs use separate vertices. Under these moves,
assume each target's indicator in a given chain is either constant or

    a_m(T) = (1 + epsilon_m(T) chi_e(s))/2,
    chi_{u,v}(s) = s_u s_v,    u != v,                  (1)

where e=e_m(T) is ONE unordered block edge and epsilon_m(T) is +1 or
-1. Unique endpoint roles give exactly this form in the chain geometry:
endpoints in the same move block are constant; those in different blocks
of one chosen label pair give (1); distinct unaffected label pairs cannot
become equal. Invariant root targets are constant, even if they have
several named witnesses.

For a target covered by the exterior or by a constant-one chain its
coverage is unchanged and certain, so omit it from the following sums.
Let n_T be the number of remaining flexible chain occurrences of T.
Constant-zero occurrences contribute nothing. There is at most one
flexible edge per target per chain. Under fully independent fair signs,

    Pr(T missed) = 2^(-n_T).                            (2)

This includes n_T=0. Let o_T be its actual old covered indicator, and put

    mu_ind = sum_T w_T [1 - 2^(-n_T) - o_T].             (3)

Thus mu_ind is the independent-move expected NET change, including old
losses. No unchanged exterior is assumed among the chains being moved.

## 2. Simultaneous interaction sampling

An interaction I pairs a block edge e in chain m with a block edge f in
a DIFFERENT chain m'. Choose a collection C of interactions such that
every physical vertex (m,u) occurs in at most one interaction. Vertices
belonging to different chains or label-pair blocks are distinct.
Choose a sign tau_I in {-1,+1} for every interaction, before sampling.

For each I sample an independent fair z_I and impose

    chi_e(s) = z_I,       chi_f(s) = tau_I z_I.          (4)

Within each of these two edges independently sample a fair sign at one
endpoint and determine the other endpoint from its prescribed parity.
Use independent fair signs at every unused vertex. All orientation
signs and all z_I are mutually independent.

Each chain's ENTIRE sign vector is still independent and uniform: each
matched edge has an independent fair parity and an independent fair
orientation, and its vertices are disjoint from other matched edges.
This remains true when the graph of interactions between chains has
cycles. The interaction law adds correlations only across chains and
does not change any individual chain's prescribed move marginal.

For a target T call I active if its two paired edges are exactly T's
flexible occurrence edges in those two chains. Write C(T) for these
interactions and r_T=|C(T)|. Their owner chains are disjoint for this
target, so 2r_T<=n_T.

## 3. Exact OR law

Under the coupled sampling above,

    Pr(T missed) = 2^(-n_T)
        product_{I in C(T)} (1 + sigma_I(T)),
    sigma_I(T) = epsilon_m(T) epsilon_m'(T) tau_I.       (5)

Proof. Expand the product of the miss factors
`(1-epsilon_m(T)chi_{e_m(T)})/2` over flexible chains. If an expanded
monomial contains an edge not itself among the interaction edges, it
has an orientation sign with mean zero. Indeed that edge joins two
distinct matched-edge or unused-vertex components in its chain. Only
one occurrence edge from this chain can appear in the monomial, so no
other factor can cancel that orientation sign; orientations in other
chains are independent. Such a monomial has expectation zero.

For a monomial using only interaction edges, every z_I must occur
either zero times or twice. It occurs twice precisely when the two
occurrence edges of an active interaction are both chosen. Their two
negative miss signs cancel, leaving sigma_I(T). Distinct interactions
have independent z_I. Summing over subsets of active interactions gives
the product in (5). The argument also handles a selected edge whose
partner is not an occurrence of T: its lone z_I kills that monomial.
This proves (5).

Consequently the exact expected NET gain is

    E Delta = mu_ind + Phi(C,tau),
    Phi = sum_T w_T 2^(-n_T)
             [1-product_{I in C(T)}(1+sigma_I(T))].      (6)

In particular some integral collection of legal phase choices has
gain at least (6). The unchanged bank is another available choice.
Equation (6) discounts an interaction by all other possible covering
chains and accounts for old-target transfer, duplicate fresh coverage,
and simultaneous loss of multiple old witnesses.

## 4. Additive regime and an explicit repeated-target penalty

For a candidate interaction I define its signed actual-target score

    J_I = sum_{T: I active for T}
                 w_T 2^(-n_T) epsilon_m(T)epsilon_m'(T). (7)

All n_T and scores refer to the SAME full fair-cut move family, before
the interactions are selected. Choose tau_I=-sign(J_I); a zero score
can use either sign. If r_T<=1 for every target, (6) is exactly

    E Delta = mu_ind + sum_{I in C}|J_I|.                (8)

Without that target-separation condition the valid lower bound is

    E Delta >= mu_ind + sum_{I in C}|J_I| - R(C),
    R(C) = sum_T w_T 2^(-n_T)(2^(r_T)-1-r_T).            (9)

To prove it, expand the product in (6). The singleton terms sum to
`-sum_I tau_I J_I`. There are `2^r-1-r` higher-degree terms, each of
absolute value one. This proves (9), with no independence or sign
assumption about different targets. For r>=2 one may also use

    2^r-1-r <= binom(r,2) 2^(r-2),                     (10)

because each subset of size at least two is counted at least once by
choosing a pair inside it. The r=0,1 contributions vanish.

A target-separated collection can be certified by an ordinary conflict
graph on candidate interactions. Join two when they share a physical
vertex OR are both active for some target. If its maximum degree is
Delta_G, greedy coloring gives Delta_G+1 feasible target-separated
classes. Hence some legal coupled update has NET gain at least

    max{0, mu_ind + [sum_I |J_I|]/(Delta_G+1)}.          (11)

These are supplied-incidence certificates. Large possible-target pools
do not prove large scores or small conflict degree. In particular it is
incorrect to add two-chain gain certificates while ignoring the product
corrections in (6).

## 5. A stationary first-step consequence

Fix the selected marked bank. Let the initial chain phases be independent
uniform phases. Conditional on that marked bank, the target domain,
weights, fixed exterior, and cut kernels must also be fixed independently
of the initial phases. In particular, weights assigned adaptively to the
old holes do NOT automatically satisfy this hypothesis. Fix each chain's
cut-block partitions and disjoint label pairs independently of those
phases. Independent fair block cuts act by
group translations on phase coordinates, so their product transition
preserves this initial product-uniform law. Equivalently this assertion
can be used with any independently acting move kernels for which the
same product stationarity has been explicitly proved.

The usual first-cell gauge causes no exception. If P_1=id and S_i is the
cut permutation in cell i, apply P_i -> P_i S_i and then normalize by the
common right gauge S_1^(-1). The new coordinates are Q_1=id and
Q_i=P_i S_i S_1^(-1) for i>=2. For fixed cut signs this is a coordinatewise
bijection of the phase space, preserving its product-uniform law.
Re-gauging changes no target equality. The parity proof uses independent
UNGauged signs; it does not impose an additional fixed first-block sign.

For each realized old bank one may select C and tau depending on its
actual target incidences. The coupling preserves that state's individual
move marginals, but its next joint law need not be a product. Stationarity
is used ONLY for the independent comparison transition:

    E_initial mu_ind = 0.                              (12)

Therefore the one-step randomized construction satisfies

    E[covered new weight] - E[covered initial weight]
        = E_initial Phi(C,tau).                        (13)

In the target-separated regime with optimized signs, the right side is
`E sum_I |J_I|>=0`. Thus the construction cannot reduce expected coverage
at this first step, and any lower bound of full physical order for this
score would give a genuine global density improvement at unchanged word
cost. General (9) gives the analogous sufficient score-minus-penalty
criterion.

One may not iterate (12) after the first coupled update: the reached
bank is correlated, so stationarity of the independent product law is
no longer the needed statement. Nor may cut partitions or move kernels
be chosen from the old phase state without proving the asserted
stationarity. Interaction selection itself may depend on that state,
because it changes the coupling but not its prescribed marginals.

## 6. What this establishes and what remains

This is an explicit simultaneous bank update, not a pairwise sum against
incompatible frozen exteriors. It is valid for literal guarded words and
counts distinct actual targets exactly. It gives a positive first-step
construction whenever the actual interaction score is large enough.

The missing asymptotic input is an economical bank and interaction family
with sufficient total score after physical-vertex conflicts and repeated
target penalties. Nothing here supplies that input, preserves every old
target, proves sustained adaptive improvement, or reduces the current
full-cube coefficient. The exact five-target transfer example in the
two-chain source is recovered by (5)--(8), but its expensive manufactured
exterior remains expensive.

## 7. Actual-bank scale audit of this sparse coupling family

The independently audited result
`/Users/amir.nuriyev/.codex/worktrees/ae28/problem/research_round1/ROUND8_WHOLE_POOL_PAIR_TRANSFER_BOUND.md`
now supplies a negative quantitative test in the accepted mark-blind
selected chain bank. For d=L=floor(log log b), h~sqrt(b), each fixed
positive Gaussian annulus satisfies

    E sup |Phi| = O(W d^4/h) = o(W).                    (14)

The supremum allows bank-dependent old phases, all disjoint label pairs,
all cell partitions, interaction choices and signs, and weights in[0,1],
but retains physical BIT-vertex nonreuse. Its proof bounds actual shared
pool labels through the selected-reference temporal law, not through a
count of available interaction slots. Complementary upper targets are
added after quotienting the automatic complement pairs in the collision
count. The same bound controls the total absolute additive score and the
repeated-target penalty in Section4.

Fixed-annulus truncation and the per-target absolute bound1/4 then give
`E sup |Phi_full|=o(4^b)` over the full valid compiled band. Thus under the
stationary first-step assumptions of Section5, THIS sparse parity coupling
cannot provide a constant density improvement in that initial marked bank.
This does not invalidate the finite coupling, bound unrestricted net gain
mu_ind+Phi, prove an iteration obstruction, or rule out dense/nonlinear
couplings and deliberately different initial banks.
