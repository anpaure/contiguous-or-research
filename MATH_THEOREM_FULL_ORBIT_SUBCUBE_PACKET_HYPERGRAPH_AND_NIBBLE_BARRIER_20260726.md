# Full-orbit subcube packets: exact hypergraph census and the growing-rank nibble barrier

Date: 2026-07-26

Method: pure mathematics only.  The valid recursive context-array factor is
used only through its exact owner partition and its simultaneous signed trace
injectivity.  No crossed recursion is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}m,
 \qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
 \qquad p_q={N_q\over W}.                                  \tag{0.1}
\]

There is an exact hypergraph formulation which does **not** force one whole
\(U_{\boldsymbol\kappa}\) option.  Its columns are arbitrary valid subcube
packets from arbitrary physical frames.  A column claims

* every middle owner of the packet; and
* a quota-marked set of mandatory literal target vertices at every signed
  depth.

The quota density at depth \(q\) is exactly \(p_q\).  After taking the full
\(S_n\)-orbit and clearing the quota denominators, every owner and every
mandatory signed-depth target has one common degree

\[
 \boxed{D=(m!)^2\sum_\alpha M_\alpha B_\alpha,}               \tag{0.2}
\]

where packet type \(\alpha\) has \(B_\alpha=2^{s_\alpha}\) owners and
\(M_\alpha\) integral quota markings.  Hence weight \(1/D\) on every
indexed column is an exact fractional perfect matching simultaneously on
all vertex classes.

Every pair codegree is also exact.  If resources of ranks \(r_a,r_b\)
intersect in \(t\) coordinates and \(I_{ab}(t)\) is their marked base-pair
census, then

\[
 \boxed{
 d_{ab}(t)=I_{ab}(t)\,
 t!(r_a-t)!(r_b-t)!(n-r_a-r_b+t)! .}                         \tag{0.3}
\]

Equivalently, with

\[
 \mathcal B=\sum_\alpha M_\alpha B_\alpha,
 \qquad
 \mathcal O_{r,s,t}
 ={n!\over t!(r-t)!(s-t)!(n-r-s+t)!},                         \tag{0.4}
\]

one has

\[
 \boxed{{d_{ab}(t)\over D}
 ={W I_{ab}(t)\over\mathcal B\mathcal O_{r_a,r_b,t}}.}       \tag{0.5}
\]

For a literal \(Q_s\) owner packet, two owners at Johnson distance \(h\)
have the particularly simple relative codegree

\[
 \boxed{{d_{00}(m-h)\over D}
 ={\binom sh\over\binom mh^2}.}                               \tag{0.6}
\]

The finer packet model evades the old whole-component variable, but it does
not enter a generic low-codegree nibble regime.  In a whole \(Q_s\) packet,
an accepted depth-\(q\) trace is incident with exactly the \(2^q\) packet
owners obtained by freely orienting its \(q\) varied pairs.  Therefore, for
either sign,

\[
 \boxed{{d_{\mathrm{end},q}\over D}=
 {2^q\over\binom{m+q}q},\qquad
 {\Delta_2\over D}\ge {2\over m+1}\quad(q=1).}               \tag{0.7}
\]

For a packet consisting only of one cyclic necklace rather than the whole
cube, the same argument gives the weaker chronological lower bound
\((q+1)/\binom{m+q}q\).  Both models give the identical depth-one barrier.

An all-depth packet column has at least \(B_{\min}\) vertices.  In the
physical-dimension convention used here, the present paired compiler is
used in the range \(H\le s/4-1\).  In particular the weaker inequality
\(s\ge2H\) certainly holds, and already gives
\(B_{\min}\ge2^{2H}\).  Consequently

\[
 \boxed{K_{\min}{\Delta_2\over D}
 \ge {2^{2H+1}\over m+1}.}                                   \tag{0.8}
\]

At \(H=A\sqrt m\), (0.8) diverges exponentially.  Thus every proposed
growing-uniformity argument whose hypothesis includes
\(K\Delta_2/D=o(1)\) is unavailable: that hypothesis is false for the
full-orbit packet hypergraph.  This does not disprove a strongly correlated
packet matching or exclude a structure-sensitive theorem with different
hypotheses.

The exact sufficient integral gate is now clean.  A matching whose middle
owner leave is \(o(W/H)\) and whose total mandatory target leave over all
signed depths is \(o(W)\) yields total coefficient-one loss \(o(W)\).
This condition is proved in Section 7.  The full orbit supplies its exact
fractional point, but (0.7)--(0.8) show that a standard small-codegree nibble
cannot be the rounding theorem.

## 1. Valid packet types and mandatory target quotas

Let

\[
 \mathcal I=\{(q,\epsilon):1\le q\le H,
                          \ \epsilon\in\{-,+\}\}.             \tag{1.1}
\]

A valid packet type \(\alpha\) consists of

1. an owner set \(P_\alpha\subseteq\binom{[n]}m\) of size
   \(B_\alpha=2^{s_\alpha}\), carrying a whole exact subcube factor;
2. for every \(a=(q,\epsilon)\in\mathcal I\), an injective literal trace
   map
   \[
     \tau_{\alpha,a}:P_\alpha\longrightarrow
     \mathcal T_a:=\binom{[n]}{m+\epsilon q}.                  \tag{1.2}
   \]

The sign convention in (1.2) is \(m-q\) for \(\epsilon=-\) and \(m+q\)
for \(\epsilon=+\).  Different packet types may use different physical
pair frames, different passive collars, and different subcube locations.
Nothing requires their owner sets to be a whole occupancy stratum.

The target vertices are *certificates*, not all physical occurrences.  An
unmarked occurrence remains in the factor and may supply harmless surplus,
but it is not consumed as a matching resource.

For every \(a=(q,\epsilon)\), choose a finite multiset of integral marked
sets

\[
                         A_{\alpha,a}\subseteq P_\alpha        \tag{1.3}
\]

such that, across \(M_\alpha\) joint all-depth markings, each
\(x\in P_\alpha\) belongs to exactly \(M_\alpha p_q\) of the sets at type
\(a\).  Such a multiset exists.  Indeed, mix uniformly all
\(\lfloor B_\alpha p_q\rfloor\)-subsets and all
\(\lceil B_\alpha p_q\rceil\)-subsets in the unique proportions giving
mean \(B_\alpha p_q\), take the Cartesian product over \(a\), and clear
the rational denominators.  Thus every marking is integral and

\[
 |A_{\alpha,a}|\in
 \{\lfloor B_\alpha p_q\rfloor,
   \lceil B_\alpha p_q\rceil\}.                               \tag{1.4}
\]

The Cartesian product is only an existence device.  A later construction
may replace it by correlated markings, provided the exact one-point counts
are retained.

## 2. The packet matching hypergraph

The vertex classes are

\[
 \mathcal V_0=\binom{[n]}m,
 \qquad
 \mathcal V_a=\{a\}\times\mathcal T_a\quad(a\in\mathcal I).  \tag{2.1}
\]

For a packet type \(\alpha\), a joint marking \(\mu\), and
\(g\in S_n\), define the column

\[
\begin{aligned}
 E(\alpha,\mu,g)
 ={}&\{(0,gx):x\in P_\alpha\}\\
 &{}\cup
 \bigcup_{a\in\mathcal I}
 \{(a,g\tau_{\alpha,a}(x)):x\in A_{\alpha,a}^{\mu}\}.
                                                                    \tag{2.2}
\end{aligned}
\]

Typed target classes make resources at different signs or depths distinct,
even when their underlying coordinate sets happen to agree.  Trace
injectivity makes every set in (2.2) a genuine hyperedge rather than a
multiset.

A matching in this hypergraph is exactly an owner-disjoint family of whole
valid packets together with noncolliding mandatory target certificates.
It is finer than a whole-\(U_{\boldsymbol\kappa}\) choice: two packets from
different frames may be selected whenever their actual owner sets are
disjoint.

The edge size is

\[
 K(\alpha,\mu)=B_\alpha+
       \sum_{a\in\mathcal I}|A_{\alpha,a}^{\mu}|,              \tag{2.3}
\]

and its marking average is

\[
 \overline K_\alpha
 =B_\alpha\left(1+2\sum_{q=1}^Hp_q\right).                    \tag{2.4}
\]

Private dummy vertices may equalize the values in (2.3) if one wishes to
apply a uniform-hypergraph theorem; this operation changes no degree or
codegree between the genuine resources.

## 3. Exact common degrees under the full coordinate orbit

### Theorem 3.1 (exact regularity)

In the indexed orbit hypergraph (2.2), every vertex in every class has the
common degree (0.2).

#### Proof

Fix a physical middle owner \(X\).  A fixed base owner maps to \(X\) under
exactly

\[
                         m!m!=(m!)^2={n!\over W}                \tag{3.1}
\]

coordinate permutations.  Packet type \(\alpha\) supplies
\(M_\alpha B_\alpha\) marked base-owner occurrences.  Summing (3.1) gives
(0.2).

Now fix \(a=(q,\epsilon)\) and \(T\in\mathcal T_a\).  Packet type
\(\alpha\) supplies exactly \(M_\alpha B_\alpha p_q\) marked base-target
occurrences.  Each maps to \(T\) under

\[
                         (m-q)!(m+q)!={n!\over N_q}             \tag{3.2}
\]

coordinate permutations.  Since

\[
 p_q{n!\over N_q}={n!\over W}=(m!)^2,                          \tag{3.3}
\]

the contribution is again \(M_\alpha B_\alpha(m!)^2\).  Sum over
\(\alpha\). \(\square\)

### Corollary 3.2 (exact fractional perfect matching)

Giving every indexed column weight \(1/D\) makes the incident weight at
every owner and every mandatory signed target exactly one.

Indexed columns which define the same physical hyperedge are parallel and
cannot both occur in an integral matching.  They do not falsify the
fractional identity: one may aggregate their weights.  If one quotients a
single marked packet orbit by its stabilizer, its vertex degrees and all
pair codegrees below are divided by that same stabilizer order.  The
relative formulae are unchanged.

## 4. Exact pair-codegree formula

Adjoin type \(0\) to \(\mathcal I\), put

\[
 r_0=m,\qquad r_{(q,\epsilon)}=m+\epsilon q,                   \tag{4.1}
\]

and interpret every owner as marked at type \(0\).  For ordered types
\(a,b\) and an admissible intersection size \(t\), let
\(I_{ab}(t)\) be the number, summed over all packet types and all joint
markings, of ordered pairs of distinct claimed base resources whose
underlying coordinate sets intersect in size \(t\).  If \(a=b\), trace
injectivity ensures that distinct base starts give distinct resources.

### Theorem 4.1 (orbit pair census)

For two fixed distinct physical resource vertices \(Z\in\mathcal V_a\),
\(Z'\in\mathcal V_b\) with \(|Z\cap Z'|=t\), their indexed codegree is
(0.3), and hence their relative codegree is (0.5).

#### Proof

The four Venn cells of an ordered pair of ranks \(r_a,r_b\) and
intersection \(t\) have sizes

\[
 t,\quad r_a-t,\quad r_b-t,\quad n-r_a-r_b+t.                  \tag{4.2}
\]

For every base pair of this orbit type, exactly the product of their four
factorials maps it to \((Z,Z')\).  Summing over the
\(I_{ab}(t)\) marked base pairs proves (0.3).  The number of physical
ordered pairs in this orbit is \(\mathcal O_{r_a,r_b,t}\) from (0.4), so
the factorial product is \(n!/\mathcal O_{r_a,r_b,t}\).  Divide by
\(D=\mathcal Bn!/W\) to obtain (0.5). \(\square\)

For a fixed first resource of rank \(r\), the size of its \((s,t)\)-shell
is

\[
 S_{r\to s}(t)=\binom rt\binom{n-r}{s-t},
 \qquad
 \mathcal O_{r,s,t}=\binom nrS_{r\to s}(t).                   \tag{4.3}
\]

Thus (0.5) may equivalently be written

\[
 {d_{ab}(t)\over D}
 ={I_{ab}(t)\over
   \mathcal B\,p_a S_{r_a\to r_b}(t)},                        \tag{4.4}
\]

where \(p_0=1\) and \(p_{(q,\epsilon)}=p_q\).  Formula (4.4) identifies
the exact local datum needed for a codegree estimate: the marked packet
pair census divided by the corresponding full Johnson shell.

## 5. Two exact specializations

### 5.1 Owner--owner pairs in one subcube

Take one literal status cell \(P\cong Q_s\).  Two owners at Hamming
distance \(h\) in its orientation coordinates have Johnson distance
\(h\), hence intersection \(m-h\).  The ordered base-pair census is

\[
                         I_{00}(m-h)=MB\binom sh.                \tag{5.1}
\]

Given one physical middle owner, the Johnson-distance-\(h\) shell has
size \(\binom mh^2\).  Substitution in (4.4) proves (0.6).  In particular,

\[
                         {d_{00}(m-1)\over D}={s\over m^2}.     \tag{5.2}
\]

For a library of packet types, (0.6) is replaced by the
\(M_\alpha B_\alpha\)-weighted average of
\(\binom{s_\alpha}h/\binom mh^2\).

### 5.2 The unavoidable owner--trace endpoint pair

Fix one whole \(Q_s\) packet and an accepted lower \(q\)-trace.  On the
\(s-q\) unvaried active pairs its containing owner is forced, while on the
\(q\) varied pairs either endpoint may be chosen.  Hence exactly \(2^q\)
owners of the packet contain the trace.  Dually, exactly \(2^q\) packet
owners lie inside an accepted upper trace.  Across the marked library
there are therefore exactly

\[
                         2^qp_q\mathcal B                          \tag{5.3}
\]

ordered accepted target--incident-owner base pairs, for either sign.  The
full coordinate group is transitive on each incidence relation.  A lower
target is contained in exactly \(\binom{m+q}q\) middle owners, and an upper
target contains the same number.  Formula (4.4) gives

\[
 {d_{a0}\over D}={2^q\over\binom{m+q}q},                      \tag{5.4}
\]

proving (0.7).  If the augmented edge contains only the \(2s\) owners of
one cyclic necklace instead of the whole cube, its consecutive window gives
\(q+1\) incident owners and therefore the corresponding lower bound with
\(q+1\) in place of \(2^q\).

This endpoint codegree is invariant under the choice of packet frames, packet
locations, quota correlations, and packet library.  It comes solely from
claiming a trace together with all owners of the whole packet.

## 6. Why the generic growing-rank nibble does not apply

The local context-array audit, in the physical-dimension convention used
here, gives \(H\le s/4-1\).  We deliberately retain only the weaker
consequence below, since it already proves the obstruction.  A packet
which carries every mandatory depth through \(H\) therefore has

\[
                         s\ge2H,
 \qquad B=2^s\ge2^{2H}.                                      \tag{6.1}
\]

Every hyperedge contains all \(B\) owner vertices, so
\(K_{\min}\ge B_{\min}\).  Combining (5.4) at \(q=1\) with (6.1) proves
(0.8).

The sharper Gaussian-window rank is also explicit.  From

\[
 p_q=\prod_{i=0}^{q-1}{m-i\over m+i+1},
 \qquad
 \log p_q=-{q^2\over m}
       +O\left({q\over m}+{q^3\over m^2}\right),              \tag{6.2}
\]

one gets, for \(H=A\sqrt m+o(\sqrt m)\),

\[
 \sum_{q=1}^Hp_q
 =(1+o(1))\sqrt m\int_0^Ae^{-x^2}\,dx.                        \tag{6.3}
\]

The floor/ceiling error in (1.4) is at most \(2H\), negligible compared
with \(B\sqrt m\).  Therefore every fixed-dimension packet column has

\[
 K=(2+o(1))B\sqrt m\int_0^Ae^{-x^2}\,dx,                     \tag{6.4}
\]

and (0.7) strengthens to

\[
 K{\Delta_2\over D}
 \ge(4+o(1)){B\over\sqrt m}
        \int_0^Ae^{-x^2}\,dx.                                 \tag{6.5}
\]

The meaning of this parameter is direct.  In a \(K\)-uniform degree-\(D\)
hypergraph, the first-order conflict count around an edge is of scale
\(KD\), while the crude pair-overlap correction can have scale
\(K^2\Delta_2\).  Their ratio is \(K\Delta_2/D\).  Hence any isolated
nibble proof which controls conflicts by this crude pair linearization
cannot apply.  Here the ratio diverges already from mandatory
owner--depth-one endpoint pairs.  No claim is made against an algorithm
which exploits the common chronological origin of those incidences.

This is a method obstruction, not a matching nonexistence theorem.  A
successful matching would have to use the chronological correlations
among the \(q+1\) endpoints rather than regard them as codegree errors.

## 7. The exact matching-cover condition sufficient for coefficient one

Let \(\mathcal M\) be any matching in the physical packet hypergraph after
parallel identical columns have been aggregated.  Define its owner and
mandatory-target leaves by

\[
 L_0=\left|\mathcal V_0\setminus\bigcup_{E\in\mathcal M}E\right|,
 \qquad
 L_T=\sum_{a\in\mathcal I}
 \left|\mathcal V_a\setminus\bigcup_{E\in\mathcal M}E\right|. \tag{7.1}
\]

### Theorem 7.1 (packet matching compiler)

If

\[
                         L_0=o(W/H),\qquad L_T=o(W),            \tag{7.2}
\]

then the selected packets give an owner-disjoint exact partial factor whose
aggregate missing signed-shadow loss through depth \(H\) is \(o(W)\).
Appending the uncovered middle owners as literal singleton words preserves
the same bound.

#### Proof

Because \(\mathcal M\) is a matching, its packet owner sets are disjoint and
its selected whole subcube factors are simultaneously legal.  Every target
vertex met by \(\mathcal M\) has a literal certified occurrence in one of
those factors.  Hence the number of uncertified mandatory targets is exactly
\(L_T\).

Appending an uncovered middle owner as a singleton does not alter any
selected packet.  In the central-word ledger, however, quarantining that
owner forfeits at most one potential occurrence at each sign and depth,
hence at most \(2H\) protected occurrences.  Charging these pessimistically
gives total loss at most

\[
                         L_T+2HL_0=o(W).                         \tag{7.3}
\]

Unmarked trace occurrences can only reduce the true target leave, so (7.3)
is an upper bound. \(\square\)

A convenient stronger classwise form is: cover a \(1-\eta_m\) fraction of
every vertex class with \(\eta_mH\to0\).  Then

\[
 L_0\le\eta_mW=o(W/H),
 \qquad
 L_T\le2H\eta_mW=o(W).                                      \tag{7.4}
\]

Thus a class-balanced near-perfect matching with relative leave
\(o(1/H)\) is sufficient.

## 8. Exact boundary

The following are proved.

1. Arbitrary subcube packets from arbitrary frames have the exact regular
   full-orbit fractional matching (0.2).
2. All pair codegrees are given by the finite packet census (0.3)--(0.5).
3. Owner pairs have the exact cube-shell ratio (0.6).
4. Owner--trace endpoint pairs force (0.7), independently of the packet
   library.
5. Since every all-depth packet has exponentially growing rank, the usual
   growing-uniformity nibble parameter diverges as in (0.8).
6. The quantitative integral statement which would suffice is precisely
   the class-balanced packet matching condition (7.2), or the stronger
   classwise form (7.4).

What is not proved is nonexistence of such a correlated matching.  The
full-orbit fractional point is exact, so there is no fractional Hall cut.
The remaining constructive theorem must be a chronological
packet-transition/absorption result which treats each trace together with
its \(q+1\) owner endpoints as one structured unit.  A generic
small-codegree nibble cannot establish it.
