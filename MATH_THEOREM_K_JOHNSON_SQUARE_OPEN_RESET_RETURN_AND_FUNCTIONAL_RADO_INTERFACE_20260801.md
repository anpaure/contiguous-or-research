# A seam-deleted Johnson square is the minimum attachment-active reset return

**Date:** 2026-08-01  
**Lane:** K, reset-conditioned functional attachment  
**Status:** independent derivation/audit of the frozen occurrence-level
four-resource theorem, plus an exact forced-bank Rado interface and a
strict-residence correction. The native three-edge square detour has a
length-two coordinate run, so for depth at least two it is **not** by
itself a strict resident flag lift. No global all-depth compiler theorem is
claimed.

## 0. Outcome

Let \(A,B\) be the two adjacent endpoint roots of an opened rolling reset.
There is a canonical Johnson square

\[
                     A-B-C-D-A
\]

through their seam. Orient the square in both directions and delete the
seam edge \(A B\) in both orientations. The two remaining three-edge
paths have:

1. the same three lower colours and the same three upper owners;
2. one head--owner alternating path with endpoints \(A,B\); and
3. two predecessor alternating paths, with endpoints
   \(A^- ,B^+\) and \(B^- ,A^+\).

These are exactly the three typed paths exported by the opened reset.
Pairing the forward reset with the reverse square, and the reverse reset
with the forward square, closes all three paths simultaneously. The seam
lower/upper pair is omitted in both phases and therefore remains one common
residual pair, rather than being consumed twice.

The full square changes the attachment permutation by a \(4\)-cycle and
the predecessor permutation by two transpositions. Its sign is therefore

\[
                         (-1,+1),
\]

the rolling-reset sign. Support four is minimum on the exact
Boolean-diamond face: support two has no nontrivial exact exchange, while a
nontrivial support-three successor permutation is a \(3\)-cycle and hence
has even attachment sign. The standard ternary Boolean hex is even more
rigid: its head--owner columns agree occurrencewise in its two phases.

There is an important quantifier correction. The phase switch changes the
functional attachment on the protected square, so one fixed global
\(\theta\) cannot describe both phases. After contracting the complete
reset--square bank, however, the residual root and owner shores are
identical. A single residual \(\theta_0\), predecessor matroid, and Rado
certificate then extend both phases, provided the deeper flag/guard
contractions are also literally common.

## 1. Canonical Johnson-square normal form

Let all roots have rank \(m\). Write the seam endpoints uniquely as

\[
             A=S\cup\{a\},\qquad B=S\cup\{b\},             \tag{1.1}
\]

where \(|S|=m-1\) and \(a,b\notin S\), \(a\ne b\). Choose

\[
                  x\in S,\qquad
                  c\notin S\cup\{a,b\},                    \tag{1.2}
\]

and put

\[
 C=(S\setminus\{x\})\cup\{b,c\},\qquad
 D=(S\setminus\{x\})\cup\{a,c\}.                         \tag{1.3}
\]

Then \(A,B,C,D\) are distinct rank-\(m\) sets and

\[
                         A-B-C-D-A                           \tag{1.4}
\]

is a Johnson \(4\)-cycle. Its four lower and upper resources are

\[
\begin{array}{c|c|c}
  \text{edge}&\text{lower intersection}&\text{upper union}\\ \hline
  AB&S&S\cup\{a,b\}\\
  BC&(S-x)\cup\{b\}&S\cup\{b,c\}\\
  CD&(S-x)\cup\{c\}&(S-x)\cup\{a,b,c\}\\
  DA&(S-x)\cup\{a\}&S\cup\{a,c\}.
\end{array}                                                  \tag{1.5}
\]

All four lower resources are distinct, and all four upper resources are
distinct. Denote the seam pair by

\[
                    L=S,\qquad U=S\cup\{a,b\}.              \tag{1.6}
\]

### Lemma 1.1 (induced-square classification)

Every induced Johnson \(4\)-cycle containing the edge \(A B\) has the form
(1.2)--(1.3), up to reversing the cycle and renaming \(x,c\). The same
conclusion holds if one assumes instead that the four cycle-edge lower
colours and the four cycle-edge upper colours are separately distinct.

#### Proof

Let \(C\ne A\) be adjacent to \(B\). If \(C=S+c\), then \(A C\) is a
chord and the two consecutive edges have the common lower colour \(S\).
If \(C=(S-x)+a+b\), then \(A C\) is again a chord and the two consecutive
edges have the common upper colour \(S+a+b\). Thus inducedness, or the
separate palette-distinctness hypothesis, forces
\(C=(S-x)+b+c\) with \(c\notin S\cup\{a,b\}\).

The common neighbours of \(A,C\) are obtained by pairing one of
\(\{x,a\}=A-C\) with one of \(\{b,c\}=C-A\). Besides \(B\), two of them
are adjacent to \(B\) and create the other chord (and the corresponding
palette repetition). The unique choice nonadjacent to \(B\) is
\(D=(S-x)+a+c\). Direct substitution gives (1.5).
\(\square\)

## 2. Delete the seam in both orientations

Orient the full square as

\[
 A\longrightarrow B\longrightarrow C\longrightarrow D
  \longrightarrow A                                             \tag{2.1}
\]

and oppositely as

\[
 B\longrightarrow A\longrightarrow D\longrightarrow C
  \longrightarrow B.                                            \tag{2.2}
\]

Delete the seam atom in both orientations. The two open phases are

\[
 \begin{aligned}
 R^+&=\{B\to C,\ C\to D,\ D\to A\},\\
 R^-&=\{A\to D,\ D\to C,\ C\to B\}.
 \end{aligned}                                                   \tag{2.3}
\]

Write \(U_{BC},U_{CD},U_{DA}\) for the three nonseam upper
resources in (1.5), and write \(L_{BC},L_{CD},L_{DA}\) for
their lower partners.

### Theorem 2.1 (exact three-return signature)

The phases \(R^+,R^-\) use the same nonseam lower and upper resources.
Their head--owner projections have symmetric difference equal to the one
alternating path

\[
       A-U_{DA}-D-U_{CD}-C-U_{BC}-B.                         \tag{2.4}
\]

Their predecessor projections have symmetric difference equal to the two
alternating paths

\[
       A^- -D^+ -C^- -B^+,\qquad
       B^- -C^+ -D^- -A^+.                                  \tag{2.5}
\]

The lower--tail projection has the additional alternating path

\[
       A-L_{DA}-D-L_{CD}-C-L_{BC}-B.                         \tag{2.5a}
\]

In particular their typed boundary currents, in the convention
\(R^- -R^+\), are

\[
\begin{array}{c|c}
 \text{shore}&\text{boundary current}\\ \hline
 \text{tail roots}& e_A-e_B\\
 \text{head roots}& e_B-e_A\\
 \text{lower colours}&0\\
 \text{upper owners}&0.
\end{array}                                                   \tag{2.6}
\]

#### Proof

Both phases use precisely the undirected edges \(BC,CD,DA\), proving the
lower/upper equality. In \(R^+\), the owner columns are

\[
 (C,U_{BC}),\quad(D,U_{CD}),\quad(A,U_{DA}),                 \tag{2.7}
\]

whereas in \(R^-\) they are

\[
 (D,U_{DA}),\quad(C,U_{CD}),\quad(B,U_{BC}).                 \tag{2.8}
\]

Alternating (2.7) and (2.8) gives (2.4).

Replacing every upper owner in that calculation by its paired lower colour
and every head by the corresponding tail gives (2.5a).

The two predecessor sets are

\[
 \{B^-C^+,C^-D^+,D^-A^+\},\qquad
 \{A^-D^+,D^-C^+,C^-B^+\}.                                 \tag{2.9}
\]

Their degree-two vertices concatenate exactly as in (2.5). The unmatched
tail and head copies give (2.6). \(\square\)

Notice that \(L,U\) from (1.6) occur in neither phase. They are one
common exposed lower/upper pair. The square does not secretly provide
them twice.

## 3. Literal composition with the opened reset

Let \(P^+,P^-\) be the two orientations of an opened reset path with
endpoint roots \(A,B\). Choose signs so that \(P^+\) runs from \(A\) to
\(B\), while \(P^-\) runs from \(B\) to \(A\). Form the phase banks

\[
             \mathcal B^+=P^+\cup R^-,\qquad
             \mathcal B^-=P^-\cup R^+.                     \tag{3.1}
\]

For the exact matching statement below, assume the two internal square
roots \(C,D\), the three nonseam lower colours, and the three nonseam upper
owners are private from the reset interior on their respective typed
shores. Also assume that the exposed seam pair \(L,U\) is not already used
inside either open reset phase. This is precisely the resource-simple
ambient embedding condition; the projection identities remain true without
it, but exactness of the union need not.

### Theorem 3.1 (square-completed reset)

At the occurrence-labelled root/lower/upper level:

1. each bank in (3.1) is a directed cycle on the reset roots together with
   \(C,D\);
2. the two banks use exactly the same tail, head, lower and upper resource
   sets;
3. the head--owner difference and the lower--tail difference are each one
   alternating cycle; and
4. the predecessor difference is the disjoint union of two alternating
   cycles.

Thus the seam-deleted square supplies one common literal lift of the reset's
attachment return and its two predecessor-parity returns. It does not use
the direct seam in either orientation, and the common seam tasks \(L,U\)
remain available to the same exterior completion.

#### Proof

The endpoint current of \(R^- -R^+\) in (2.6) is the negative of the
endpoint current of \(P^- -P^+\), because the square phases are paired
crosswise in (3.1). Hence every tail and head has degree one in each bank.
The lower and upper currents vanish separately in both the reset and the
square.

At the projection level, the reset attachment path and (2.4) have the same
typed endpoints and opposite phase colours, so their union is an
alternating cycle. The reset lower--tail path is closed by (2.5a), and the
same statement applied to each path in (2.5) closes the two reset
predecessor-parity paths. Every projected edge came from the same literal
oriented Johnson atom, so these projection cycles are not independently
paired: they are one occurrence-labelled lift.
\(\square\)

The resulting two directed cycles are reversals of the same undirected
cycle. Consequently every cyclic contiguous-window union multiset and
every cyclic contiguous-window intersection multiset is the same in the
two phases. This gives raw all-width shadow transparency of the closed
component. It does **not** assert that all of those windows have the ranks
required by a strict depth-\(d\) compiler.

## 4. Why support four is the exact central minimum

The rolling reset has attachment sign \(-1\) and predecessor sign \(+1\):
on its even ring the attachment changes by one even-length cycle, while the
predecessor changes by a shift of two and hence by two parity cycles.

Call an exact trade an **orientation-flip trade through a seam atom**
\((L,U;E,F)\) if its old phase contains that atom, its new phase contains
\((L,U;F,E)\), and both phases are four-resource matchings with the same
typed resource sets.

### Theorem 4.1 (support minimum)

Among orientation-flip trades through one seam atom, support four is the
minimum capable of the reset sign \((-1,+1)\).

#### Proof

At support two, equality of the tail and head sets forces the other old
atom to be the opposite seam orientation \((L,U;F,E)\), since the new
phase already contains it and only the two roots \(E,F\) are available.
The old phase then repeats both \(L\) and \(U\), contrary to being a
four-resource matching.

At support three, let the common tail set be \(\{E,F,A\}\) and the common
head set be \(\{F,E,B\}\).  Since neither phase may also contain the
opposite seam orientation, the two remaining old atoms must be

\[
                            F\to B,\qquad A\to E,
\]

and the two remaining new atoms must be

\[
                            E\to B,\qquad A\to F.
\]

Thus \(A\) is a common Johnson neighbour of \(E,F\).  The common-neighbour
dichotomy says that the edges \(AE,AF\) share either the seam lower colour
\(L\) or the seam upper colour \(U\).  In the former case the old or new
phase repeats \(L\); in the latter it repeats \(U\).  Hence one phase fails
to be a four-resource matching.  This excludes support three without
identifying the predecessor permutation with the attachment permutation.
For the particular ternary Boolean hex the failure is stronger: the three
head--owner columns agree occurrencewise in the two phases, so its
attachment action is the identity.

For the full Johnson square, comparing (2.1) and (2.2) assigns the four
owners to heads by a \(4\)-cycle, of sign \(-1\). The predecessor assignment
changes by the square of that cycle, namely two transpositions, of sign
\(+1\). Hence support four attains the required sign. \(\square\)

There is a complementary path-level minimum. A two-edge detour between
adjacent \(A,B\) repeats either its lower colour or its upper owner: a common
neighbour is either \(S+g\), repeating the lower \(S\), or
\((S-f)+a+b\), repeating the upper \(S+a+b\). The three-edge detour
\(B-C-D-A\) in (1.3) is the shortest one internally injective on both
palettes.

## 5. Exact functional-\(\theta\)/Rado interface

The square does not preserve the attachment pointwise. On its open bank,

\[
\begin{array}{c|ccc}
 R^+&\theta(C)=U_{BC}&\theta(D)=U_{CD}&\theta(A)=U_{DA}\\
 R^-&\theta(D)=U_{DA}&\theta(C)=U_{CD}&\theta(B)=U_{BC}.
\end{array}                                                   \tag{5.1}
\]

Thus it is incorrect to put both phases under one fixed global
\(\theta\). The correct operation is forced-bank contraction.

### Theorem 5.1 (common residual Rado criterion)

Suppose the two banks \(\mathcal B^+,\mathcal B^-\) from (3.1) have literal
flag lifts such that:

1. their declared marked suffix/guard resource multisets agree;
2. every atom meeting a phase-dependent protected resource is placed in
   the corresponding forced bank or deleted from the exterior ground;
3. after contracting the phase bank and restricting to one
   occurrence-labelled exterior ground, the residual aligned-column
   systems and predecessor lists are identical; and
4. their common exposed seam tasks \(L,U\) have the same residual menus.

Let \(\theta_0:Q'\to O'\) be a legal bijection on that common residual
root/owner shore. Then one residual completion extends **both** square-reset
phases if and only if

\[
 r_{M_P}\left(\bigcup_{q\in Y}\mathcal A_{\theta_0}(q)\right)
                         \ge |Y|
                    \qquad(Y\subseteq Q').                  \tag{5.2}
\]

Here \(M_P\) is the common residual predecessor transversal matroid.

#### Proof

Theorem 3.1 says the two forced banks consume the same typed resource sets;
hypotheses 1--4 promote this immediate equality to equality of the complete
contracted exterior instance. Rado's independent-transversal theorem on
that common instance gives (5.2). Adjoining either phase bank to the same
residual transversal uses every tail, head and owner once and covers the
same declared targets. Conversely, any common residual completion gives
an independent representative from every column family, so Rado necessity
gives (5.2). \(\square\)

The theorem fixes \(\theta_0\) only **after** deleting the protected bank.
It neither asserts nor needs equality of the two phase attachments in
(5.1).

### Corollary 5.2 (dual-flow and gammoid use)

The same statement holds in the tail-functional form after fixing a common
residual owner-to-tail bijection \(\phi_0\). In a literal phase-exchange
network, the complete square-reset flip may be represented as one compound
exchange arc. It may enter the reset-contracted strict-gammoid/Rado router
provided different routed copies are occurrence-resource-disjoint and its
terminal target payload is included in the common contraction. The three
projection paths may not be entered as three unrelated arcs: their common
square atoms are the reason the literal lift is valid.

## 6. The first surviving obstruction: native depth-\(d\) residence

The coordinate \(c\) in (1.2) belongs to \(C,D\) and to neither endpoint
\(A,B\). Hence on either open orientation its occurrence word is

\[
                              0\,1\,1\,0.                    \tag{6.1}
\]

### Proposition 6.1 (length-two run obstruction)

Under the repository convention that strict depth-\(d\) residence requires
every positive run to have length at least \(d+1\), the raw square detour is
not a resident consecutive segment for any \(d\ge2\).

#### Proof

Equation (6.1) is a maximal one-run of length two, independent of what lies
outside the segment because both endpoints omit \(c\). For \(d\ge2\), the
required floor \(d+1\) is at least three. Reversing the path does not change
(6.1). \(\square\)

If one checks only the one-coordinate deletion-word shift at depth two,
the local word \(f,x,g\) can look legal; that weaker check is not the
repository's residence condition. Exact depth-two residence still asks for
run length three and therefore fails on (6.1). For every \(d\ge2\), the
square needs a nonlocal/nonflat collar, a longer occurrence route, or a flag
rethread which changes the literal intermediate roots. Therefore
Theorem 5.1 is an exact functional-interface theorem, not yet a resident
all-depth Boolean host theorem.

## 7. Scope and dependencies

The occurrence identities, sign calculation, support minimum, and run
obstruction are uniform in \(m\) whenever (1.2) is nonempty. No finite
search is used. The result does not prove exterior residence, compiler
common-cap safety, voltage, a regenerative supply of disjoint squares, or
the all-\(k\) upper bound.

It sharpens the current phase-paired search as follows:

\[
 \boxed{\text{one Cartesian gain ear per phase: common-support no-go}}
 \quad\longrightarrow\quad
 \boxed{\text{one seam-deleted support-four square: exact functional return}}
 \quad\longrightarrow\quad
 \boxed{\text{nonlocal resident/common-minor lift still required}}.
\]

The input interfaces are:

* MATH_THEOREM_BOOLEAN_JOHNSON_SQUARE_OPEN_THREE_RETURN_MACRO_20260801.md
  (source construction and independent finite replay);
* MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md;
* MATH_THEOREM_K_PROTECTED_FUNCTIONAL_RADO_FACE_AND_LITERAL_TRIANGLE_EXCHANGE_OBSTRUCTION_20260801.md;
* MATH_THEOREM_K_RESET_CONTRACTED_DUAL_FUNCTIONAL_FLOW_AND_RADO_PHASE_ROUTER_20260801.md;
* MATH_THEOREM_OPPOSITE_SEAM_CARTESIAN_GAIN_EAR_COMMON_RESIDUAL_NOGO_20260801.md;
* MATH_THEOREM_BOOLEAN_HEX_THREE_CYCLE_FUSION_AND_TERNARY_CONTRACTION_20260801.md; and
* MATH_THEOREM_L_TWO_SIDED_COORDINATE_COVER_FG_HEX_DETOUR_AND_THREE_RETURN_GATE_20260801.md.
