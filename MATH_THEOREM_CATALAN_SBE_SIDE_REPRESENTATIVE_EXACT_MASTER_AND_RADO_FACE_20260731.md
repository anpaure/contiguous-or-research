# SBE side representatives: an exact joint master, the Rado face, and the owner-alignment obstruction

Date: 2026-07-31  
Status: exact all-parameter Boolean formulation and exact polynomial Rado
face; literal independently replayed counterexample to SBE plus
\(\eta^\pm\ge3\) at parameter \(n=3\). Existence on the authenticated
recursively produced SBE parents at \(n=5,6,7\) remains open.

## 0. Verdict

Strict balanced expansion (SBE) and the facet slack

\[
                         \eta^\pm(F)\ge 3                         \tag{0.1}
\]

do not by themselves form a representative theorem. They control
different projections:

* SBE is a weighted Hall condition on the two palette occurrence graphs;
* \(\eta^\pm\) is a singleton lower bound in the raw physical occurrence
  multigraph; and
* the contracted graphic row is a rank condition on every physical
  vertex set.

This note makes the gap exact.

1. There is one literal \(0\)-\(1\) master which jointly chooses the
   component orientation, the common puncture set \(Q\), both side
   representatives, all physical degree caps, and the uncontracted form of
   the contracted graphic row. Its SBE cuts have two min-cut separation
   oracles, and its physical forest cuts have the usual graphic separation
   oracle.
2. After an orientation and \(Q\) are fixed, forgetting one palette and
   the overlapping degree caps gives exactly Rado's theorem in the rooted
   Higgs or augmented graphic matroid. The maximum partial completion has
   an explicit min--max formula.
3. The full selector is not this matroidal face. It contains two palette
   partition bases, a graphic row, and a nonmatroidal degree-two row. The
   family of linear forests already violates the matroid exchange axiom on
   five vertices.
4. The proposed implication is literally false already at \(n=3\). There
   is a direct-diamond parent for which both shores are SBE and
   \((\eta^-,\eta^+)=(3,3)\), yet none of its fifteen common co-singleton
   bases admits even one degree-capped side representative. Every puncture
   has a unique palette-perfect acyclic selector, and its unique
   degree-two centre is a seam anchor.

The finite obstruction identifies the missing row more sharply than a
generic graphic-rank failure: one needs a **puncture-correlated owner
reserve**. A positive theorem for the recursively produced SBE chain must
choose \(Q\) and the representative matching so that every forced
degree-two physical centre is outside the anchor set, before asking for the
contracted graphic row.

## 1. An exact conservation master

Let \(F\) be an undirected Catalan path forest at parameter \(n\). Use

\[
 M={2n\choose n},\quad N={2n\choose n-1},\quad
 P={2n\choose n-2},\quad C=M-P.                       \tag{1.1}
\]

Choose a reference orientation on every nontrivial component. For a
child edge \(q\), let

\[
       (t_q^0,h_q^0),\qquad (t_q^1,h_q^1)=(h_q^0,t_q^0) \tag{1.2}
\]

be its endpoints in the two coherent orientations of its component.
Write \(z_i\in\{0,1\}\) for the chosen orientation of component \(i\).

For every child edge and orientation state introduce \(a_{q,b}\in\{0,1\}\).
It means that \(q\in Q\) and its component has orientation \(b\). Put

\[
 r_q=a_{q,0}+a_{q,1},                                 \tag{1.3}
\]

and impose

\[
 a_{q,0}\le1-z_i,\qquad a_{q,1}\le z_i
       \quad(q\in E(P_i)).                            \tag{1.4}
\]

The raw upper occurrence \(e=(q,x)\), \(x\notin U_q\), has

\[
 d^-(e)=L_q+x,\quad o^-(e)=U_q+x,\quad
 \partial^-(e)=\{t_q^0+x,h_q^0+x\}.                  \tag{1.5}
\]

The physical edge in (1.5) is orientation-independent. The raw lower
occurrence \(e=(q,x)\), \(x\in L_q\), has

\[
 o^+(e)=L_q-x,\quad d^+(e)=U_q-x,\quad
 \partial^+(e)=\{t_q^0-x,h_q^0-x\}.                  \tag{1.6}
\]

Let \(s_e^-,s_e^+\in\{0,1\}\) select side occurrences.

### Theorem 1.1 (palette conservation eliminates the hidden common basis)

For a fixed undirected parent, orientation, puncture set and side
occurrences have both exact outer palettes and both exact punctured middle
palettes if and only if (1.3)--(1.4) and the following equations hold:

\[
\begin{aligned}
 \sum_{e:o^-(e)=V}s_e^-&=1
       &&\left(V\in{\Omega\choose n+2}\right),\\
 \sum_{e:d^-(e)=D}s_e^-+
 \sum_{q,b:t_q^b=D}a_{q,b}&=1
       &&\left(D\in{\Omega\choose n}\right),         \tag{1.7}\\
 \sum_{e:o^+(e)=A}s_e^+&=1
       &&\left(A\in{\Omega\choose n-2}\right),\\
 \sum_{e:d^+(e)=D}s_e^++
 \sum_{q,b:h_q^b=D}a_{q,b}&=1
       &&\left(D\in{\Omega\choose n}\right).        \tag{1.8}
\end{aligned}
\]

In particular, these equations force

\[
                    |Q|=\sum_qr_q=M-P=C,              \tag{1.9}
\]

and \(Q\) is a common basis of the two strict pulled-back transversal
duals. No separate common-basis rank inequalities are needed in the
integral master.

#### Proof

For an oriented path forest, the tail map on child edges and the head map
on child edges are injective. The second line of (1.7) partitions every
middle colour between one selected upper occurrence and one selected tail
of \(Q\). Its first line uses every upper outer colour exactly once. This
is precisely the strict upper puncture equation. The two lines of (1.8)
give the lower equation with heads. Summing either middle-colour family
gives \(P+|Q|=M\), proving (1.9). Conversely, exact puncture and outer
palettes give every displayed equation. The coupled SDR normal form then
identifies \(Q\) as a common basis. \(\square\)

The simultaneous endpoint SBE rows are added directly in the orientation
variables \(z_i\): for every closed middle set \(A\) on each shore,

\[
 C|A\cap Z^\sigma(z)|\ge
 N|O^\sigma(A)|-R|A|,\qquad \sigma\in\{-,+\},         \tag{1.10}
\]

with complementary endpoint choices on the two shores. For fixed \(z\),
two ordinary min-cuts separate (1.10).

### Theorem 1.2 (literal physical completion of the master)

Form the expanded canonical direct-collar multigraph before any forest
contraction. It contains every raw side occurrence edge, both oriented
seam variants for each child edge, the punctured structural rail, and all
fixed rail fragments. Give each potential physical edge \(f\) its literal
indicator

\[
 \chi_f(a,s)\in\{0,1\}.                               \tag{1.11}
\]

Thus a side edge has indicator \(s_e^\sigma\), an oriented seam has
indicator \(a_{q,b}\), a retained structural edge has indicator \(1-r_q\),
and a fixed edge has indicator one. Then the complete undirected direct
support is a linear forest if and only if

\[
 \sum_{f\ni v}\chi_f(a,s)\le2
                    \qquad(v\text{ a physical vertex}),          \tag{1.12}
\]

and

\[
 \sum_{f\in E(W)}\chi_f(a,s)\le |W|-1
                    \qquad(\varnothing\ne W\subseteq V).         \tag{1.13}
\]

Consequently (1.3)--(1.13), with integrality, are an exact joint master for

    endpoint SBE + common Q + both side palettes
    + every physical degree cap + the complete contracted graphic row.

#### Proof

All indicators in (1.11) are literal edge-presence indicators in the
uncontracted construction. Inequality (1.12) is exactly maximum physical
degree two. For an integral multigraph, (1.13) for all nonempty vertex
sets is exactly graphic independence; the two-vertex rows also exclude
parallel two-cycles. Contracting fixed forest fragments preserves cycle
rank, so this uncontracted condition is equivalent to the usual contracted
attachment-graph row. The direct recursive support theorem now applies
to the palettes from Theorem 1.1. \(\square\)

For an integral candidate, (1.12)--(1.13) are checked by degrees and
union--find. Fractional graphic separation is also polynomial. This does
not make the whole master integral: the endpoint cover and the two-palette
selector are genuine integer correlations.

## 2. The exact polynomial face and its min--max

Fix an orientation and \(Q\). On one shore let \({\cal M}\) be the relevant
physical matroid:

* the rooted Higgs lift for an upper no-empty shore; or
* after fixing the upper shore, the augmented graphic matroid for the
  lower topology row.

For one palette coordinate \(\xi\), let \({\cal C}_\xi\) be its \(P\) colours
and \({\cal E}_c\) the occurrence menu of colour \(c\).

### Theorem 2.1 (Rado min--max face)

The maximum number of \(\xi\)-colours representable by a set independent in
\({\cal M}\) is

\[
 \boxed{
 \nu_\xi(Q)=
 \min_{J\subseteq{\cal C}_\xi}
 \left(P-|J|+
 r_{\cal M}\!\left(\bigcup_{c\in J}{\cal E}_c\right)\right).}
                                                               \tag{2.1}
\]

In particular, this one-coordinate physical selector is complete if and
only if

\[
 r_{\cal M}\!\left(\bigcup_{c\in J}{\cal E}_c\right)\ge|J|
                       \qquad(J\subseteq{\cal C}_\xi).          \tag{2.2}
\]

#### Proof

This is the defect form of Rado's theorem, equivalently ordinary matroid
intersection between the palette partition matroid and \({\cal M}\).
Deleting the colours outside \(J\) gives the upper bound in (2.1), and the
Rado inequalities give equality. \(\square\)

Formula (2.1) is the maximal immediate ordinary-matroid face. A private
complete-ear reserve also lies on this face. If slot \(i\) has a menu
\({\cal P}_i\) of internally palette-complete, cap-safe ears, different
slots use disjoint physical and palette resources, and \(\sigma(P)\) is the
suppressed quotient edge of an ear, then all slots can be filled exactly
when

\[
 r_{\cal G}\!\left(\bigcup_{i\in J}\sigma({\cal P}_i)\right)
       \ge |J|\qquad(J\subseteq I).                  \tag{2.3}
\]

This is the exact protected-reserve theorem available after SBE: first
choose an SBE orientation, then a common \(Q\) which exposes such a private
bank, and finally apply (2.3). Neither SBE nor (0.1) supplies that bank.

There is one slightly larger clean face. Suppose every complete private
packet is an element of both a unit-gated socket gammoid
\({\cal M}_{L}\) and the quotient graphic matroid \({\cal M}_{G}\), with
both palettes and all degree caps compiled privately inside the packet.
If \(h\) packets are required on common ground \({\cal P}\), Edmonds'
matroid-intersection min--max is exact:

\[
 \max\{|I|:I\in{\cal I}({\cal M}_{L})\cap{\cal I}({\cal M}_{G})\}
 =\min_{X\subseteq{\cal P}}
       \bigl(r_G(X)+r_L({\cal P}\setminus X)\bigr).    \tag{2.4}
\]

Thus this protected packet bank is complete exactly when every right side
in (2.4) is at least \(h\). This is the maximal presently identified
ordinary matroid/gammoid face. Its privacy and unit-gated hypotheses are
load-bearing; the full atomic occurrence problem is outside it. The
classification and its determinant-two parity minor are proved separately
in

    MATH_THEOREM_CATALAN_SBE_REPRESENTATIVE_GRAPHIC_GAMMOID_FACE_AND_PARITY_OBSTRUCTION_20260731.md

## 3. Why the full face is not ordinary matroid intersection

For fixed \(Q\), exactness of both side palettes is the intersection of two
partition bases on the occurrence ground. The rooted/augmented graphic
row contributes a third matroid. The physical degree row is not itself a
matroid.

### Proposition 3.1 (five-vertex exchange obstruction)

Let the physical ground contain the edges of the following two linear
forests on vertices \(1,2,3,4,5\):

\[
 A=\{12,23\},\qquad B=\{13,24,25\}.                  \tag{3.1}
\]

Both are acyclic and have maximum degree at most two, and \(|A|<|B|\).
But no edge of \(B\setminus A\) can be added to \(A\): edge \(13\) closes
the triangle \(1,2,3\), while either \(24\) or \(25\) gives vertex \(2\)
degree three. Hence the family

\[
        \{S:\partial S\text{ is acyclic and }\Delta(\partial S)\le2\}
                                                               \tag{3.2}
\]

fails the matroid exchange axiom. In particular it is not a gammoid.

This rules out treating the physical row as the one additional matroid in
a Rado proof. It does not rule out a special extended formulation using
the direct Boolean geometry. It shows exactly where such a formulation
would have to add information.

The endpoint layer has a separate integrality issue: its supermodular
cover over endpoint-pair equations has a feasible half-integral one-pair
example with no integral endpoint choice. Therefore simply placing the
endpoint cover and the physical graphic polytope in a generalized
polymatroid intersection is not an integrality proof either.

## 4. Literal failure of SBE plus facet slack

The independently replayed \(n=3\) fixture in

    MATH_THEOREM_CATALAN_SBE_ETA3_SIDE_REPRESENTATIVE_N3_COUNTEREXAMPLE_20260731.md

is a direct-diamond parent, not an abstract relabelling. Its fifteen atoms
have exact rank-two and rank-four palettes and form five directed paths on
the twenty rank-three vertices. Both raw facet-continuation histograms are

    3^5 4^5 5^5,

so

\[
                         (\eta^-,\eta^+)=(3,3).        \tag{4.1}
\]

Both shores pass every one of their \(2^6=64\) SBE rows with parameters

\[
                         (M,N,P,C,R)=(20,15,6,14,1).  \tag{4.2}
\]

Consequently the constant \(14/15\) vector lies in both direct base
polytopes. In this fixture every co-singleton

\[
                         Q_r=E(F)\setminus\{r\},
                         \qquad r=0,\ldots,14,         \tag{4.3}
\]

is a common basis.

### Theorem 4.1 (owner-alignment obstruction)

For every \(Q_r\) and on each shore, the punctured occurrence graph has
exactly one palette-perfect representative matching. It is physically
acyclic, but exactly one seam anchor has selected side degree two. The
overload-owner rows are

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
r&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
\text{upper}&12&6&6&7&12&6&7&11&11&11&7&12&1&1&1\\
\text{lower}&9&13&13&5&9&13&5&3&3&3&5&9&4&4&4 .
\end{array}                                           \tag{4.4}
\]

Neither row has a fixed point. Under \(Q_r\), the only physical palette
vertex not made a seam anchor is the vertex owned by \(r\). Therefore the
unique degree-two centre is always anchored, violates its cap one, and
cannot be changed by a graphic or gammoid exchange because no alternative
palette matching exists.

Hence

\[
 \boxed{\mathrm{SBE}^-\wedge\mathrm{SBE}^+
        \wedge\eta^-\ge3\wedge\eta^+\ge3}
 \quad\not\Longrightarrow\quad
 \boxed{\text{degree-capped side representatives}}.   \tag{4.5}
\]

The failure occurs before the contracted graphic row: all thirty unique
palette matchings in the two-shore puncture census are already acyclic.

#### Proof

The literal replay reconstructs every atom, both SBE systems and both
physical occurrence quotients. It then exhausts all six-colour perfect
matchings for all fifteen punctures and obtains one matching per shore and
puncture, with the overload owners (4.4). Since the owner never equals
\(r\), that degree-two vertex is one of the fourteen anchors. The cap
failure is therefore forced. \(\square\)

The missing protected reserve is now exact. A candidate common basis must
be correlated with the representative matching so that every forced
degree-two centre belongs to the unanchored owner bank. More generally, if
\(c_y(S)\) denotes the selected side degree at physical palette vertex
\(y\) and \(r_y\) is the unique child edge owning \(y\), the literal cap is

\[
                         c_y(S)+{\bf1}_{r_y\in Q}\le2. \tag{4.6}
\]

SBE supplies uniform one-edge marginals for \(Q\), but it controls neither
the joint events in (4.6) nor the existence of an alternative matching.
This owner-alignment reserve is the first missing row before private ears
or contracted topology can help.

## 5. Exact remaining theorem

The universal implication is closed negatively by Theorem 4.1. The
narrower theorem for the authenticated recursively produced SBE parents
at \(n=5,6,7\) remains open. Its state cannot use only singleton physical
slack. A sufficient recursive state must provide at least one of the
following genuinely correlated objects.

1. A common \(Q\) together with representative menus satisfying the
   two-palette equations (1.7)--(1.8) and all literal forest cuts
   (1.12)--(1.13).
2. A puncture-correlated owner reserve satisfying (4.6), followed by a
   protected private-ear bank satisfying the rank rows (2.3), with both
   palettes and all caps compiled inside each ear.
3. A direct-geometry theorem proving owner-aligned alternatives, the
   relevant physical rank, and an augmenting exchange property.

SBE remains valuable: it certifies a balanced common-basis face and gives
additive averaging on \(Q\). Condition (0.1) remains valuable: it excludes
forced raw physical vertices. The literal fixture shows why neither one is
a replacement for the correlated physical representative state.

The literal counterexample is independently replayed by

    scratch/audit_catalan_sbe_eta3_physical_counterexample_n3_20260731.py
    scratch/catalan_sbe_eta3_physical_counterexample_n3_20260731.audit.json
