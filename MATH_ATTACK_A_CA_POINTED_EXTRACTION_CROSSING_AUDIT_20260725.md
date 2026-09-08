# Pointed extraction versus residual cyclic crossing: exact two-endpoint defect

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

## 0. Verdict

The finite pointed-extraction theorem in
MATH_ATTACK_H_POINTED_CYCLIC_FLAG_EXTRACTION_20260725.md is sound as a
theorem about signed literal shoulder targets.  In particular, its signed
spill identity, fibre cap, same-parent collision estimate, and cloned Hall
argument all survive independent checking.

It does not by itself prove the residual common-cover theorem.  There are
two exact losses when its output is projected to the lower-rank quota
problem.

1. The signed targets S at slot -q and [n]\S at slot q+1 are distinct
   targets in the extraction matching, but both project to the same lower
   q-set S.  Separate degree caps u_q therefore become a projected cap
   2u_q, and signed global distinctness need not remain lower-rank
   distinctness.

2. A lower pointed occurrence records the head of one literal cyclic
   two-endpoint edge.  A directed residual Hall cut needs an edge entering
   the cut.  Occurrences whose other endpoint is also in the cut are
   useless for that cut.  The extraction theorem controls total head
   incidence, not this signed edge boundary.

The main new result below makes the second loss exact.  At every depth q,
one exact factor induces a multigraph G_q having one actual owner-edge per
middle owner and two literal cyclic endpoint targets.  For a fixed balanced
quota b_q, put

    d_q(F,b)=max_U ( e_q(U)-b_q(U) )_+.

Then d_q is exactly the minimum number of off-endpoint assignments in the
complete-off relaxation.  Equivalently,

    d_q(F,b)
      =max_U ( b_q(U)-e_q(U)-|delta_q(U)| )_+.

Every literal Boolean or common nested completion has at least this many
off-endpoint assignments.  More strongly, its off-endpoint owner set must
meet the internal and external owner packets displayed in Theorem 4.3.
All floors remain inside

    b_q(U)=c_q|U|+|H_q intersect U|.

At depth one, every zero canonical fibre contributes its full positive
balanced quota to an unavoidable interior-facet burden.  Precisely, any
balanced depth-one assignment has at least

    sum_S ( b_1(S)-2 ell_1(S) )_+

interior-facet assignments.  This burden is invisible to pointed
extraction because a target of canonical load zero has no pointed
occurrence to extract.

Thus the audited extraction removes neither the two-endpoint cut defect nor
the remaining legal-extension/common-owner problem.  The exact unproved
gate is now a signed-boundary extraction theorem together with a legal
common extension of its unmatched owner and quota slots.  No fixed-window
alignment or constant-one conclusion is claimed.

## 1. Common notation

Put

    n=2m+1,
    V_q=C([n],m-q),
    W=C(n,m).

Fix one oriented exact middle wreath factor F.  Every middle owner X is a
unique cyclic interval I_P(j,m) in its actual row P.  Its canonical target
at depth q is

    Gamma_q(X)=I_P(j,m-q).

For q>=1 define the other endpoint child of the canonical parent by

    Lambda_q(X)=I_P(j+1,m-q).

Both Gamma_q(X) and Lambda_q(X) are children of

    Gamma_(q-1)(X)=I_P(j,m-q+1).

They are distinct throughout the fixed Gaussian window.

Let

    ell_q(S)=#{X:Gamma_q(X)=S}.

Fix integral balanced quotas belonging to one common feasible nested flag
flow:

    b_q(S)=c_q+1_(S in H_q),
    c_q=floor(W/|V_q|),
    |H_q|=W-c_q|V_q|.

Consequently, for every U subset V_q,

    b_q(U)=c_q|U|+|H_q intersect U|.                 (1.1)

No proportional replacement of (1.1) will be made.

## 2. Cross-audit of the pointed-extraction theorem

### 2.1 Signed spill

For the upper signed slot a=q+1,

    [n]\Z_(q+1)(P,j)=I_P(j+m+q+1,m-q).

The shift of the pointed start is a permutation of all starts in every
row.  Hence upper signed loads are exactly the depth-q lower loads after
complementation.  Relabelling a minimizing lower balanced quota gives a
minimizing upper quota with the same overload O_q(F).  The two signed slots
are separate target systems, so counting O_q twice when both slots are
used is correct for the signed theorem.

The equality between total positive excess and total positive deficit is
also exact: both the load vector and the balanced quota have total W.

### 2.2 Fibre cap

For a fixed lower fibre of load mu and a balanced quota beta<=u_q,

    beta-min(mu,u_q)
      <= (beta-mu)_+

after taking the positive part.  Summing first over any prescribed target
family and then over all deficits proves

    sum_(S in U) min(ell_q(S),u_q)
       >= c_q|U|-O_q(F).

The same statement applies to the complemented upper family.  Capping
only designates occurrences; it neither removes a wreath nor changes
middle ownership.

### 2.3 Same-parent collision averaging

For two nested signed targets separated by g ranks, conditional on the
lower relabelled target, the added g-set is uniform among exactly

    C(n-|lower target|,g)

choices.  The denominator used in the extraction report is a valid uniform
lower bound over the fixed window.  The fixed-dimensional product-parent
property gives the stated numerator.

There is no measurability gap from choosing capped occurrences after the
coordinate relabelling: capped prescribed incidences form a subset of all
prescribed incidences.  Therefore their same-parent pair count is bounded
pointwise by the uncapped same-parent pair count to which the averaging
argument is applied.

### 2.4 Hall integrality

After pruning, every selected start of degree at least s has at least s
incident edges, while every signed target has degree at most Delta_A.  For
any set J of such starts,

    s|J| <= e(J,N(J)) <= Delta_A |N(J)|.

Thus |N(J)|>=floor(s/Delta_A)|J|.  Clone every start that many times.  For
an arbitrary subset of clones, project to its underlying starts; the
number of clones is at most the clone multiplicity times the number of
projected starts, while its neighbourhood is unchanged.  Hall therefore
matches every clone integrally.  This verifies the step for arbitrary
clone subsets, not only unions of complete clone classes.

The extraction theorem is therefore valid with its stated signed-target
scope.

## 3. Exact projection losses

### Lemma 3.1 (complementary signed fibres merge)

Fix q>=1 and S in V_q.  Under the lower-rank projection

    Pi_q(S at slot -q)=S,
    Pi_q(T at slot q+1)=[n]\T,

the two signed target fibres S and [n]\S both have load ell_q(S).
Separate caps in the signed theorem permit as many as

    2 min(ell_q(S),u_q)

designated incidences over the projected fibre S.  In particular the
projected degree can be 2u_q, and a matching may use both signed targets
even though they are one lower-rank target.

If instead one imposes the correct joint projected cap u_q, the retained
number in this paired fibre is

    min(2ell_q(S),u_q).

For every U subset V_q the following universal spill bound remains valid:

    sum_(S in U) min(2ell_q(S),u_q)
       >= c_q|U|-O_q(F),                              (3.1)

The separate signed lower bound with twice the right side does not follow
under this joint cap; indeed, when c_q>=2 and ell_q(S)=c_q, the joint
fibre has size u_q<=c_q+1<2c_q while its spill is zero.

#### Proof

The complement identity gives the two equal loads.  The first assertions
are then immediate.  For (3.1),

    min(2ell_q(S),u_q)>=min(ell_q(S),u_q),

and the audited one-fibre cap inequality from Section 2.2 applies.  This
proves (3.1).  \square

Thus signed distinctness and signed supply cannot be imported unchanged
as lower-rank quota distinctness and supply.

### Lemma 3.2 (which owner a pointed target exposes)

Fix a pointed start (P,j).

For every q>=1, the lower target

    Z_(-q)(P,j)=I_P(j,m-q)

is the endpoint sibling Lambda_q(X^-) for the one common owner

    X^-=I_P(j-1,m).

Moreover X^- belongs to the directed singleton crossing set for that
target at every depth q.

For the upper target, put

    S_q=[n]\Z_(q+1)(P,j)
       =I_P(j+m+q+1,m-q).

The owner whose canonical endpoint edge enters S_q is

    X_q^+=I_P(j+m+q,m),

which depends on q.  There is one fixed root

    Y^+=I_P(j+m+1,m)

whose repeated left-endpoint deletion path visits every S_q, but for q>=2
its canonical parent Gamma_(q-1)(Y^+) does not contain S_q.  Hence Y^+ is
not a member of the canonical directed singleton crossing set at those
depths.

#### Proof

All identities follow by substituting interval starts and lengths.  For
the last assertion, Gamma_(q-1)(Y^+) starts at j+m+1, whereas S_q starts q
positions later and contains the next coordinate beyond the right end of
that canonical parent.  Thus containment fails for q>=2.  \square

Consequently only the lower half of one pointed flag directly supplies one
common owner to the canonical crossing packets at every depth.  The upper
half is a coherent literal reverse flag, but it is not a common canonical
packet membership certificate.  Treating its H incidences as H canonical
crossing memberships of one owner is invalid.

## 4. The cyclic two-endpoint multigraph

For each q>=1 define the multigraph G_q on V_q.  It has one edge e_X for
each actual middle owner X, with endpoints

    Gamma_q(X), Lambda_q(X).                           (4.1)

Parallel edges are retained because their owners are distinct.  There are
exactly W edges.  For U subset V_q write

    e_q(U)=#{X:Gamma_q(X),Lambda_q(X) both lie in U},

and let delta_q(U) be the multiset edge boundary of U.

### Lemma 4.1 (exact fibre degree)

For every S in V_q,

    deg_(G_q)(S)=2ell_q(S).                            (4.2)

#### Proof

An occurrence S=I_P(j,m-q) is the Gamma endpoint of the owner at start j
and the Lambda endpoint of the owner at start j-1 in the same row.  These
owners are distinct.  Conversely every incident owner-edge yields one of
these two occurrences.  Different row occurrences yield different middle
owners because the factor has exact middle ownership.  \square

### Theorem 4.2 (exact complete-off defect)

Let G=(V,E) be any finite loopless multigraph and let

    b:V to Z_(>=0),  sum_v b(v)=|E|.

An endpoint assignment sends an edge to one of its two endpoints.  In the
complete-off relaxation an edge may instead be sent to any quota slot and
is then charged one off-endpoint unit.  Let tau_off(G,b) be the minimum
number of charged edges.  Then

    tau_off(G,b)
      =max_(U subset V) ( e_G(U)-b(U) )_+             (4.3)

      =max_(U subset V)
          ( b(U)-e_G(U)-|delta_G(U)| )_+.             (4.4)

In particular tau_off=0 if and only if

    e_G(U)<=b(U)<=e_G(U)+|delta_G(U)|                 (4.5)

for every U subset V.

#### Proof

Replace every vertex v by b(v) quota clones.  Form a bipartite graph whose
left vertices are the edges of G and in which a left edge is adjacent to
all clones of its two endpoints.  Let M be a maximum matching.  The
standard Hall-deficiency formula gives

    |E|-|M|
       =max_(Q subset E)( |Q|-b(N(Q)) )_+.            (4.6)

If U=N(Q), then every member of Q has both endpoints in U, so

    |Q|-b(N(Q))<=e_G(U)-b(U).

Conversely, for a fixed U take Q=E_G(U), the set of all edges internal to
U.  Its endpoint neighbourhood is contained in U, whence

    |Q|-b(N(Q))>=e_G(U)-b(U).

Maximizing proves (4.3).

Match the |M| matched edges to their endpoint quota clones.  The unmatched
edges and unmatched quota clones have the same cardinality |E|-|M|; in the
complete-off relaxation pair them arbitrarily.  This realizes exactly the
deficiency in (4.6).  Conversely, the endpoint-assigned part of any
complete-off assignment is a matching in the clone graph, so no assignment
uses fewer charged edges.  This proves the equality with tau_off.

Finally, with T=V\U,

    e_G(T)-b(T)
      =b(U)-e_G(U)-|delta_G(U)|,

because |E|=e_G(U)+e_G(T)+|delta_G(U)| and b(V)=|E|.
Taking maxima over complements proves (4.4), and (4.5) follows.  \square

The equality in Theorem 4.2 is deliberately stated for the complete-off
relaxation.  In a literal Boolean assignment an off-endpoint owner may use
only a legal descendant, and in a common flag resolution these legal
choices must concatenate through all depths.  Therefore Theorem 4.2 gives
an exact relaxation value and a rigorous lower bound for the literal
problem.  Equality in the literal problem additionally requires the
unmatched owners and unmatched quota clones of some maximum endpoint
matching to have a perfect matching in the legal incidence graph.  That is
an additional Hall condition, not a consequence of (4.3).

### Proposition 4.2A (exact legal extension boundary)

For the factor F at depth q, let

    L_q(X)={S in V_q:S subset X}

be the legal rank-q descendants of the middle root X.  Define

    tau_leg(q;F,b)

to be the minimum number of off-endpoint owners among all maps psi with

    psi(X) in L_q(X),
    #{X:psi(X)=S}=b_q(S).

If no such map exists, set tau_leg=infinity.  Then

    tau_leg(q;F,b)>=d_q(F,b).                          (4.6a)

Equality holds if and only if some maximum matching M in the endpoint
clone graph from Theorem 4.2 has the following extension property: after
deleting the owners and quota clones matched by M, the remaining owners
have a perfect matching to the remaining quota clones through the legal
incidences S in L_q(X).

Equivalently, for that maximum M, if Q_M is its unmatched owner set and
R_M is the multiset of unmatched quota clones, then

    |N_leg(Q) intersect R_M|>=|Q|                     (4.6b)

for every Q subset Q_M.

#### Proof

The endpoint part of any legal assignment is a matching in the endpoint
clone graph.  It has at most the maximum matching size, proving (4.6a).
If equality holds, the endpoint part has maximum size and the off-endpoint
part is exactly a legal perfect matching between the two unmatched sides;
Hall gives (4.6b).  Conversely, append such a legal perfect matching to M.
Exactly the unmatched |E|-|M|=d_q owners are off-endpoint, proving
equality.  \square

Thus the legal rank-q problem is exactly a zero-one min-cost bipartite
matching problem: legal endpoint incidences have cost zero and all other
legal incidences have cost one.  Network integrality gives an integral
optimum.  Proposition 4.2A identifies precisely when its optimum collapses
to the simpler maximum-cut value.  A common nested resolution imposes the
additional requirement that the chosen legal assignments at successive
depths concatenate; rankwise equality in (4.6a) is not sufficient for
that.

### Theorem 4.3 (literal internal and external owner packets)

Let a legal rank-q assignment of the W rooted paths have final load b_q.
Let J_q be the owners whose assigned q-target is neither endpoint in
(4.1).  Then for every U subset V_q,

    |J_q intersect E(G_q[U])|
       >= (e_q(U)-b_q(U))_+,                          (4.7)

    |J_q intersect E(G_q[V_q\U])|
       >= (b_q(U)-e_q(U)-|delta_q(U)|)_+.             (4.8)

Consequently

    |J_q|>=d_q(F,b),                                  (4.9)

where d_q is either maximum in (4.3)--(4.4).

If the canonical paths outside an exceptional owner family E are frozen,
then J_q subset E.  Hence the same packet inequalities hold with E in
place of J_q, and |E|>=d_q(F,b).

#### Proof

Every internal owner-edge not in J_q is assigned to one of its endpoints,
both of which lie in U.  Since only b_q(U) paths in total may finish in U,
at least e_q(U)-b_q(U) internal edges must be off-endpoint.  This proves
(4.7).

There are e_q(U)+|delta_q(U)| owner-edges with at least one endpoint in U.
If b_q(U) exceeds this number, every further path finishing in U comes from
an owner-edge with both endpoints outside U and is necessarily
off-endpoint.  This proves (4.8).  Formula (4.9) follows.  A frozen owner
outside E remains at Gamma_q(X), one of its endpoints, so every member of
J_q lies in E.  \square

Equations (4.7)--(4.8) are literal packet demands on actual middle owners;
they do not merely compare marginal histograms.

### Corollary 4.4 (depth-one interior-facet burden)

At q=1 an off-endpoint assignment is exactly an assignment of a middle
owner to one of the m-2 non-endpoint facets of its cyclic middle interval.
Every balanced depth-one assignment satisfies

    |J_1|
       >= sum_(S in V_1)(b_1(S)-2ell_1(S))_+.         (4.10)

In particular every zero canonical fibre S forces b_1(S) distinct
interior-facet assignments.  Therefore

    |E|>=sum_S(b_1(S)-2ell_1(S))_+                   (4.11)

for every frozen-exception completion.

#### Proof

By Lemma 4.1, exactly 2ell_1(S) owners have S as one of their two cyclic
endpoint facets.  Among the b_1(S) distinct owners assigned to S, at least

    (b_1(S)-2ell_1(S))_+

therefore use an interior facet.  The owner families counted for different
assigned targets S are disjoint, so the bounds sum.  Every such owner is
noncanonical and hence exceptional.  \square

For m>=3 one has c_1=1, but (4.10) retains the exact choice of the high
quota set H_1 and does not replace b_1 by its mean.

## 5. Exact split of the directed crossing packets

For A subset V_q define the endpoint-visible incoming crossing set

    C_q^end(A)
      ={X:Gamma_q(X) notin A, Lambda_q(X) in A}.

This is exactly the directed edge boundary of A in G_q when every
owner-edge is directed from Gamma to Lambda.  Define

    C_q^off(A)=C_q(A)\C_q^end(A),

where C_q(A) is the full canonical crossing-owner set in the residual Hall
theorem.  An owner in C_q^off(A) has a canonical parent containing at least
one member of A, but its other cyclic endpoint child is not in A; entering
A at that canonical transition requires a non-endpoint child.

### Proposition 5.1 (exact off-endpoint directed demand)

For every exceptional family E satisfying the residual Hall inequality,

    |E intersect C_q^off(A)|
      >= ( |C_q(A)|-kappa_q^b(A)
           -|E intersect C_q^end(A)| )_+              (5.1)

      >= ( |C_q(A)|-kappa_q^b(A)
           -|C_q^end(A)| )_+.                         (5.2)

Here, exactly,

    kappa_q^b(A)
      =c_(q-1)|N_q(A)|-c_q|A|
       +|H_(q-1) intersect N_q(A)|-|H_q intersect A|. (5.3)

#### Proof

The two crossing sets form a disjoint partition of C_q(A).  Substitute
that partition into the exact directed Hall inequality

    |E intersect C_q(A)|>=|C_q(A)|-kappa_q^b(A)

and isolate the off-endpoint term.  Formula (5.3) is the exact balanced
collar identity.  \square

For a singleton S, occurrence rotation gives

    |C_q^end({S})|=ell_q(S).                           (5.4)

At depth one,

    |C_1({S})|-kappa_1^b({S})=b_1(S)-ell_1(S),

so (5.2) becomes

    |E intersect C_1^off({S})|
       >=(b_1(S)-2ell_1(S))_+,                        (5.5)

in agreement with Corollary 4.4.

## 6. Why pointed extraction does not control the new packets

For a lower target family A, the total pointed incidence counted by the
extraction cap is

    ell_q(A)=#{X:Lambda_q(X) in A},                   (6.1)

after rotating owner starts by one position.  The useful canonical
crossing incidence is only

    |C_q^end(A)|
      =#{X:Lambda_q(X) in A, Gamma_q(X) notin A}.     (6.2)

The difference consists of edges internal to A.  The cap and the target
degree bound control (6.1), not (6.2).  Even maximal head incidence gives
no lower bound on the directed boundary: taking A=V_q gives incidence W
and boundary zero.  More locally, a union of components of G_q has zero
boundary regardless of its positive pointed incidence.

The Hall matching in the extraction theorem addresses a different cut
system.  It matches selected starts to distinct signed target names.  It
does not orient every actual owner-edge to meet the exact quotas b_q, and
it does not impose

    e_q(U)<=b_q(U)<=e_q(U)+|delta_q(U)|.              (6.3)

The prime-equivariant common flag flow makes the full Boolean collars
kappa_q^b nonnegative.  It does not imply (6.3) for the factor-dependent
multigraphs G_q, nor does it bound the off-endpoint term in (5.2).

The verified fixed-order star collar also does not bound these quantities
for arbitrary connected Hall cores.  In particular a singleton lower
target has order m-q, outside the fixed-order hypothesis.

## 7. Quantitative consequence for fixed-window alignment

Let P_X(q) be the q-target of root X in any common balanced nested
resolution, and put

    a_q=#{X:P_X(q) != Gamma_q(X)}.

Every off-endpoint assignment is changed, so Theorem 4.3 gives

    a_q>=|J_q|>=d_q(F,b).                              (7.1)

Therefore every labelled fixed-window alignment satisfies the exact lower
bound

    sum_(q<=H) a_q/c_q
       >= sum_(q<=H) d_q(F,b)/c_q.                    (7.2)

Thus a necessary condition for the pointed-extraction route to prove
labelled fixed-window alignment is

    min_(F,b common) sum_(q<=H)d_q(F,b)/c_q=o(W).     (7.3)

No estimate of the form (7.3) follows from the audited extraction theorem.
Its unsigned capped mass may be large while one of the signed cut defects
in (4.3)--(4.4) is large.

Even (7.3) would not finish the argument.  Three further compatibility
requirements remain:

1. some maximum endpoint matchings must leave owner and quota slots which
   admit legal Boolean inclusion matchings;
2. those legal matchings must concatenate through all depths using one
   common owner identity system;
3. the resulting exceptional owners must meet the full off-endpoint
   directed demands (5.1), as well as the survival packets.

An exact conditional composition is available.  Apply pointed extraction
only to the lower signed slots, and let J be the selected pointed starts.
Replace every j in J by its predecessor owner X^-(j).  If the resulting
owner family E satisfies all survival inequalities and, for every q and A,

    |E intersect C_q^end(A)|+|E intersect C_q^off(A)|
       >=|C_q(A)|-kappa_q^b(A),                       (7.4)

then the exact residual Hall theorem supplies an integral common nested
completion.  If |J|=o(W/H), this has the required exceptional-owner scale.

Condition (7.4), however, is precisely the signed-boundary/common-cover
statement absent from pointed extraction.  The extraction theorem proves
many distinct heads, not (7.4).

## 8. Precise proved and unproved boundary

### Proved

1. The pointed signed extraction theorem passes the four requested audit
   checks.
2. Complementary signed targets merge under the lower-rank CA projection;
   the separate caps and distinctness do not survive unchanged.
3. The exact complete-off defect of the actual cyclic two-endpoint
   multigraph is the maximum floor-sensitive cut distance (4.3)--(4.4).
4. Every literal completion obeys the internal and external owner-packet
   inequalities (4.7)--(4.8) and the full directed off-endpoint inequality
   (5.1).
5. The depth-one zero-fibre/interior-facet lower bound (4.10) is exact and
   additive over target fibres.
6. Every labelled alignment obeys the quantitative lower bound (7.2).

### Unproved

The required theorem is still:

> For every fixed A, choose one exact factor F, one common balanced quota
> flow b, and o(W/sqrt(m)) owners which simultaneously meet the survival
> packets, the endpoint-visible directed boundaries, and the off-endpoint
> directed packets through q<=ceil(A sqrt(m)).

Equivalently, one first needs a factor/common-flow pair for which the cut
defect sum in (7.3) is o(W), and then a legal common extension theorem for
the unmatched slots.  Neither assertion is proved here.

### Adversarial audit of the new theorem

1. The equality in Theorem 4.2 is for the explicitly defined complete-off
   relaxation.  It is only a lower bound for literal Boolean inclusion;
   no maximum zero-edge matching is assumed extendible.
2. All multigraph edges retain their actual owner labels and parallel
   multiplicities.
3. Every floor and high-quota correction remains in b_q(U) and in the
   collar (5.3).
4. The upper signed reverse flag is literal, but it is not falsely counted
   as one canonical crossing owner at all depths.
5. The signed complementary-fibre collision is not hidden by global target
   distinctness: the two target sets have different ranks before
   projection and one lower identity afterward.
6. Separate feasibility of (6.3) at different q would still not provide a
   common nested owner resolution; no such inference is made.
7. The packet lower bounds are necessary conditions, not a constructed bad
   exact factor.  Hence they close the direct unsigned-extraction
   implication but do not disprove CA_A.
