# Independent counting audit of the all-radius rotor master circuit

Date: 2026-07-24

## 1. Verdict

The submitted multiplicity ledger is arithmetically correct, including the
exceptional radii (d=m-1,m).  With

\[
 Q_m=(2m-1)(2m)!,
\]

the normal-radius repetition numbers produce exactly
(Q_mc_d/|\Omega_d|) designated occurrences of every state, the final
permutation circuit produces the same prescribed multiplicities, and the
number of transition entries is exactly (Q_mW).

There are two wording qualifications.

1. A mask has exactly (Q_m) **designated post-transition endpoint
   occurrences**.  Initialization creates additional incidental endpoint
   witnesses, so the total number of actual witnesses need not equal
   (Q_m).
2. At formal depth (q=m), the lower endpoint is the empty set.  It is not
   the OR of a nonempty interval in a nonzero word.  The counting statement
   is an OR statement for every **nonempty** mask; the empty endpoint may be
   retained only as a formal symmetric-chain endpoint.

This note audits counting and multiplicity.  Existence/strong connectivity
of each asserted Eulerian rotor component is a separate structural claim.

## 2. State count

A radius-(d) state consists of a middle set (S), an ordered list of
(d) distinct elements of (S), and an ordered list of (d) distinct
elements of (S^c).  Hence

\[
 |\Omega_d|
 =\binom{2m}{m}(m)_d^2
 =\frac{(2m)!}{(m-d)!^2}.
\tag{2.1}
\]

The same formula gives

\[
 |\Omega_{m-1}|=|\Omega_m|=(2m)!.
\tag{2.2}
\]

This equality is genuine.  At (d=m-1), the two residual cores are
singletons; at (d=m), they are formally empty.  In both cases the ordered
last-occurrence partition is equivalent to a permutation of the (2m)
coordinates.

## 3. Exact incidence of a fixed endpoint mask

Put

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

Coordinate transitivity already implies a constant fibre.  A direct lower
endpoint count is also useful.  Fix (A) of size (m-q), where (q\le d).
Choose the (q) elements restoring the middle set, order those first
departures, complete the remaining (d-q) departure annotations, and choose
the (d) arrival annotations.  This gives

\[
 \binom{m+q}{q}q!
 \frac{(m-q)!}{(m-d)!}
 \frac{m!}{(m-d)!}
 =\frac{(m-q)!(m+q)!}{(m-d)!^2}
 =\frac{|\Omega_d|}{N_q}.
\tag{3.1}
\]

The upper endpoint count is identical.  At (q=0), there is one middle
endpoint per state and the fibre is

\[
 \frac{|\Omega_d|}{W}
 =\left(\frac{m!}{(m-d)!}\right)^2.
\tag{3.2}
\]

Within one state, the advertised masks have different ranks and hence are
distinct.  A fixed mask occurs at most once at a given endpoint state.

## 4. Quota coefficients

Define

\[
 c_d=N_d-N_{d+1},\qquad N_{m+1}=0.
\tag{4.1}
\]

Then

\[
 \sum_{d=q}^{m}c_d=N_q,
 \qquad
 \sum_{d=0}^{m}c_d=N_0=W.
\tag{4.2}
\]

The terminal values, where an off-by-one error would be most damaging, are

\[
 c_{m-1}=\binom{2m}{1}-\binom{2m}{0}=2m-1,
 \qquad
 c_m=\binom{2m}{0}-0=1.
\tag{4.3}
\]

## 5. Normal radii (0\le d\le m-2)

Let

\[
 k_d=(m-d)^2
\]

be the in- and outdegree.  One directed Euler traversal has

\[
 k_d|\Omega_d|
\]

arcs and visits every state exactly (k_d) times as an arc head.  Repeat it

\[
 a_d=(2m-1)c_d(m-d-1)!^2
\tag{5.1}
\]

times.  The state multiplicity is

\[
\begin{aligned}
 a_dk_d
 &=(2m-1)c_d(m-d-1)!^2(m-d)^2\\
 &=(2m-1)c_d(m-d)!^2\\
 &=\frac{Q_mc_d}{|\Omega_d|}.
\end{aligned}
\tag{5.2}
\]

The number of transition entries at radius (d) is therefore

\[
 a_dk_d|\Omega_d|=Q_mc_d.
\tag{5.3}
\]

All repetition numbers and state multiplicities are integers.

## 6. The exceptional permutation circuit

At the final two radii use the directed move-to-front graph on all
((2m)!) singleton permutations.  Its degree is (2m-1), so an Euler
circuit has

\[
 (2m-1)(2m)!=Q_m
\]

arcs and visits every permutation (2m-1) times as a head.

Use (2m-1=c_{m-1}) full traversals with the radius-((m-1))
interpretation and one (=c_m) traversal with the radius-(m)
interpretation.  The resulting state multiplicities are

\[
 (2m-1)^2
 =\frac{Q_mc_{m-1}}{|\Omega_{m-1}|}
\tag{6.1}
\]

and

\[
 2m-1
 =\frac{Q_mc_m}{|\Omega_m|}.
\tag{6.2}
\]

The final circuit contributes

\[
 2mQ_m=Q_m(c_{m-1}+c_m)
\tag{6.3}
\]

transition entries.  Thus there is no missing factor (2m-1) or (2m)
at the exceptional radii.

The two interpretations of a singleton permutation are compatible.  The
radius-((m-1)) chain consists of its prefix sets of ranks (1,ldots,2m-1),
whereas the formal radius-(m) chain adds the empty and full endpoints.

## 7. Total transition and initialization lengths

Summing (5.3) and (6.3),

\[
 \sum_{d=0}^{m}Q_mc_d=Q_mW.
\tag{7.1}
\]

There is one initialized block for each (d=0,ldots,m-2), containing
(2d+2) nonempty blocks, and one shared all-singleton initialization of
size (2m) for (d=m-1,m).  Therefore

\[
 \sum_{d=0}^{m-2}(2d+2)+2m
 =m(m-1)+2m
 =m^2+m.
\tag{7.2}
\]

This convention initializes the starting state and then traverses every arc
of the Euler circuit.  The endpoint after each transition is designated;
the initial pre-transition endpoint is not part of the exact quota ledger.

Consequently the constructed word length in this convention is

\[
 Q_mW+m^2+m.
\tag{7.3}
\]

## 8. Endpoint multiplicity

Fix a target of rank (m-q) or (m+q), with (q\le m).  Its number of
designated endpoint occurrences contributed by radius (d\ge q) is

\[
 \frac{|\Omega_d|}{N_q}
 \frac{Q_mc_d}{|\Omega_d|}
 =\frac{Q_mc_d}{N_q}.
\tag{8.1}
\]

Summing over all eligible radii and using (4.2),

\[
 \sum_{d=q}^{m}\frac{Q_mc_d}{N_q}=Q_m.
\tag{8.2}
\]

The same calculation at (q=0) gives exactly (Q_m) designated middle
occurrences per middle mask.

Every designated occurrence lies at a different chronological endpoint
position.  They are not distinct states or distinct masks: repeated Euler
traversals deliberately revisit both.  Initialization may create further
incidental suffix witnesses, so (8.2) should not be advertised as an exact
count of *all* witnesses in the literal word.

As a global consistency check, each type-(d) state advertises (2d+1)
formal chain masks, and telescoping gives

\[
 \sum_{d=0}^{m}(2d+1)c_d
 =W+2\sum_{q=1}^{m}N_q
 =2^{2m}.
\tag{8.3}
\]

Thus the designated incidence total agrees with (Q_m) times the number of
Boolean masks, including the formal empty endpoint.  For the nonzero OR
problem, delete that single target from the interpretation; no construction
cost or other multiplicity changes.

## 9. Exact status

The following claims pass the independent audit:

* the size of every state layer;
* every fixed-mask incidence fibre;
* all (c_d) values and telescoping sums;
* all normal-radius repetition counts;
* the exceptional (m-1,m) permutation multiplicities;
* the transition total (Q_mW);
* the initialization total (m^2+m); and
* exactly (Q_m) designated post-transition endpoints per nonempty mask.

The only corrections are to distinguish designated from incidental witnesses
and to exclude the empty formal endpoint from the nonzero contiguous-OR
claim.
