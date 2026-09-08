# Six promotion frames: a mixed-placeholder rectangle, exact floor descent, and the support-minimality obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

**Superseding result.**  The later theorem
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`
constructs a three-top full-frame exchange whose two shores are both
squarefree and have identical middle support, while retaining nonzero
positive-depth floor action.  The present note remains a correct audit
of the one-base mixed-placeholder rectangle, but its favorable fixed
collar starts with middle collisions and is not the minimal legal
primitive.

Put

\[
 n=2m,\qquad M=m+H,\qquad H=o(m),
\tag{0.1}
\]

and assume, harmlessly for the asymptotic application, that

\[
 M>6H+3,\qquad m-H\ge 5.
\tag{0.2}
\]

There is an explicit compound replacement of six actual cyclic frames
which keeps one frame at every touched top and has a nonzero, phasewise
action at every interval length.  It uses three positional placeholders
and transports no singleton character: its first nonzero external-label
character is the pair rectangle

\[
 \eta
 =e_{\{x_5,z\}}-e_{\{x_0,z\}}
   +e_{\{x_0,w\}}-e_{\{x_5,w\}},
 \qquad \|\eta\|_2^2=4,
\tag{0.3}
\]

whose point boundary is zero.

More precisely, choose a common \((M-3)\)-set \(C\), distinct labels

\[
 x_0,x_1,\ldots,x_5,z,w\notin C,
\tag{0.4}
\]

and three positions \(A,B,D\) in a common cyclic positional word on
\(C\cup\{A,B,D\}\).  For \(0\le i\le4\), use the top

\[
 U_i=C\cup\{x_i,x_{i+1},z\},
\tag{0.5}
\]

and use

\[
 U_5=C\cup\{x_5,x_0,w\}.
\tag{0.6}
\]

The old frame puts \((x_i,x_{i+1},s_i)\) in \((A,B,D)\), where
\(s_i=z\) for \(i<5\) and \(s_5=w\); the new frame swaps the entries
in \(A,B\) and fixes the entry in \(D\).

For every positional interval, both in direct form and after adjoining
the varying roots, the aggregate six-frame derivative is exactly

\[
 \boxed{\quad \Delta=d_w-d_z,\quad}
\tag{0.7}
\]

where \(d_t\) is the derivative of swapping \(A,B\) on the virtual
closing top

\[
 V_t=C\cup\{x_5,x_0,t\}.
\tag{0.8}
\]

Thus (0.7) remains exact after arbitrary common phase deletion, common
phase weights, and a common phase-to-depth tag schedule.  In direct form
it is nonzero precisely on intervals containing \(D\) and exactly one of
\(A,B\); in root form it is nonzero precisely on intervals excluding
\(D\) and containing exactly one of \(A,B\).  In either case its
nonzero coefficient is a context lift of (0.3), with the appropriate
sign.

Choose the three placeholder positions with pairwise cyclic distance
greater than \(2H\).  For every full root-form \(h\)-deck with

\[
                         2\le h\le2H,
\tag{0.9}
\]

and, by global complementation, for every direct \((M-h)\)-deck,

\[
 \boxed{
 \|\Delta_h\|_2^2=8h,
 \qquad
 \sum_{i=0}^5\|c_{i,-}^h-c_{i,+}^h\|_2^2=24h.}
\tag{0.10}
\]

Hence the compound move cancels exactly two thirds of the separate
six-frame restitution while retaining a nonzero load direction.

The old and new six-frame packets have equal intrinsic floor energy.
Nevertheless there is an exact state-adaptive descent.  Keep the virtual
closing top \(V_z\) fixed in its minus frame.  For the floor-corrected
half energy

\[
 \Phi_c(L)=\frac12\sum_T(L_T-c)(L_T-c-1),
\tag{0.11}
\]

where \(c\) is any integer baseline, replacing the six old frames by the
six new frames changes the full \(h\)-deck energy by

\[
 \boxed{
 \Phi_c(L_{\rm new})-\Phi_c(L_{\rm old})=-2h
 \qquad(2\le h\le2H).}
\tag{0.12}
\]

The same one physical choice of seven frames gives (0.12)
simultaneously at every such length.  In the usual two-sided depth-\(q\)
flag, apply it separately to \(h=H-q\) and \(h=H+q\); the degenerate
full decks \(h=0,1\) have zero action.

The descent has a precise ownership interpretation.  Among the seven
old root-form \(h\)-decks there are exactly \(2h\) pairwise target
collisions and no triple collision; the seven new decks are pairwise
disjoint.  Thus at the middle length \(h=H\) the move repairs exactly
\(2H\) internal owner collisions.  In particular the favorable old
shore is not itself a middle-owner matching.  If “preserves middle
ownership” is required to mean that both shores lie inside an already
collision-free exact owner factor, this construction does **not** meet
that stronger requirement; rather, it proves an exact floor-repair
direction and isolates the collision that pays for its descent.

There is also a sharp limitation.  In the whole common-base
three-placeholder swap library, if the singleton boundary is zero but
the pair boundary is nonzero, then its squared pair norm is at least
four, and consequently its full short-deck action is at least \(8h\).
The construction attains equality.  But it is **not** a genuinely
six-supported load primitive: equation (0.7) factors it through two
closing-top swaps.  Indeed the same pair rectangle is already realized
by two opposed swaps with spectators \(z,w\).  If the \(z\)-closing top
must remain fixed, a two-edge \(z\)-path and the \(w\)-closing edge use
only three changed tops and give the same derivative and the same collar
descent.

Therefore, absent an additional owner-disjointness or protected-top
condition, there is no meaningful assertion that six is the smallest
support.  What is proved is an optimal first higher-character direction,
an exact all-depth descent in a literal local state, and a rigorous
factorization no-go for treating it as a new irreducible six-top atom.
No global collision-free packing or coefficient-one theorem is claimed.

## 1. Direct and root-form interval columns

Let

\[
 Z=[n]\setminus C.
\tag{1.1}
\]

Fix a cyclic positional word \(\omega\) on
\(C\cup\{A,B,D\}\).  If \(P\) is any positional interval, write

\[
 K=P\cap C,
 \qquad S=P\cap\{A,B,D\}.
\tag{1.2}
\]

For a top \(U\), a frame \(\pi\), and the root
\(R=[n]\setminus U\), use the two literal target vectors

\[
 v^{\rm dir}_{U,\pi}(P)=e_{\pi(P)},
 \qquad
 v^{\rm root}_{U,\pi}(P)=e_{R\cup\pi(P)}.
\tag{1.3}
\]

The second expression is the promotion root form.  Global
complementation sends it to the direct vector of the complementary
positional interval:

\[
 [n]\setminus(R\cup\pi(P))=\pi(P^c).
\tag{1.4}
\]

Consequently every direct identity has a root-form dual, with \(P\)
replaced by \(P^c\).

For \(t\notin C\cup\{x_0,x_5\}\), let \(V_t\) be (0.8).  Its plus
frame puts

\[
                         (x_5,x_0,t)
\tag{1.5}
\]

in \((A,B,D)\), and its minus frame puts

\[
                         (x_0,x_5,t)
\tag{1.6}
\]

there.  Denote either its direct or root-form phase derivative by

\[
 d_t(P)=v_{V_t,-}(P)-v_{V_t,+}(P).
\tag{1.7}
\]

The form in use will always be stated or clear from context.

## 2. The exact six-frame telescope

### Theorem 2.1 (phasewise mixed-spectator identity)

For every positional interval \(P\), in both direct and root form,

\[
 \sum_{i=0}^5
 \left(v_{U_i,-}(P)-v_{U_i,+}(P)\right)
 =d_w(P)-d_z(P).
\tag{2.1}
\]

#### Proof

First give all six directed edges

\[
 x_0x_1,x_1x_2,\ldots,x_4x_5,x_5x_0
\tag{2.2}
\]

the common spectator \(z\).  Regard \(z\) as part of the common base.
If \(P\) contains neither or both of \(A,B\), each swap has zero
derivative.  If it contains \(A\) but not \(B\), the direct derivatives
telescope as

\[
 \sum_{i\pmod6}
 \left(e_{K'\cup\{x_{i+1}\}}
       -e_{K'\cup\{x_i\}}\right)=0,
\tag{2.3}
\]

where \(K'\) is the common contribution of \(C\) and, when present,
\(z\).  The only-\(B\) case is the negative of (2.3).  Thus the complete
common-\(z\) cycle has zero direct derivative, phase by phase.

Replace only its closing \(z\)-edge by the closing \(w\)-edge.  The
change in the derivative is exactly \(d_w(P)-d_z(P)\), proving (2.1)
in direct form.  Apply global complementation (1.4) to prove the
root-form identity. \(\square\)

Because (2.1) is phasewise, summing it with arbitrary common real weights
proves the following immediately.

### Corollary 2.2 (all-depth literal legality)

Replace the plus frame by the minus frame on each of the six distinct
tops \(U_i\).  This keeps exactly one actual cyclic frame on every
touched top.  Identity (2.1) holds separately at every interval length,
after every common phase restriction, and under every common
phase-to-depth schedule.

This is root-balanced legality.  It does not assert that an independently
specified global middle matching remains collision-free; that is a
separate positive embedding condition.

## 3. The first nonzero character

Let \(L_K^{(r)}\) denote adjoining the fixed context \(K\) to a vector
on \(r\)-sets.  Define \(\eta\) by (0.3).

### Lemma 3.1 (singleton cancellation and pair rectangle)

For a direct positional interval with placeholder set \(S\), the
six-frame derivative is

\[
 \Delta^{\rm dir}(K,S)=
 \begin{cases}
   L_K^{(2)}\eta,&S=\{A,D\},\\
   -L_K^{(2)}\eta,&S=\{B,D\},\\
   0,&\text{otherwise}.
 \end{cases}
\tag{3.1}
\]

In root form it is the globally complemented context lift

\[
 \Delta^{\rm root}(K,S)=
 \begin{cases}
   -\mathcal C L_{C\setminus K}^{(2)}\eta,&S=\{A\},\\
   \mathcal C L_{C\setminus K}^{(2)}\eta,&S=\{B\},\\
   0,&\text{otherwise},
 \end{cases}
\tag{3.2}
\]

where \(\mathcal C e_Q=e_{[n]\setminus Q}\).

Moreover

\[
 \partial_1\eta=0,
 \qquad
 \sum_Q\eta_Q=0,
 \qquad
 \|\eta\|_2^2=4.
\tag{3.3}
\]

#### Proof

If \(S\) contains exactly \(A\) among \(A,B\) and excludes \(D\),
the derivative is

\[
 \sum_{i\pmod6}
 (e_{K\cup\{x_{i+1}\}}-e_{K\cup\{x_i\}})=0.
\tag{3.4}
\]

If it also contains \(D\), the five \(z\)-edges give

\[
 e_{K\cup\{x_5,z\}}-e_{K\cup\{x_0,z\}},
\tag{3.5}
\]

and the \(w\)-edge gives

\[
 e_{K\cup\{x_0,w\}}-e_{K\cup\{x_5,w\}}.
\tag{3.6}
\]

Their sum is the first line of (3.1).  Exchanging \(A,B\) changes the
sign, and all remaining cases have zero derivative.  Formula (3.2)
follows from (1.4), because complementing \(S\) exchanges the two cases
in (3.1).

The four pairs in (0.3) are distinct.  At each of
\(x_0,x_5,z,w\), the two incident coefficients cancel.  This proves all
three statements in (3.3). \(\square\)

Thus the exchange is not another singleton-profile move.  It lies in the
integer pair cycle space and is nonzero there.

## 4. Exact short-deck norm

Choose \(A,B,D\) so that each of the three cyclic gaps between consecutive
chosen positions is greater than \(2H\).  This is possible under (0.2).
Every interval of length at most \(2H\) then contains at most one
placeholder.

For a frame \(\pi\) on top \(U\), write

\[
 c_{U,\pi}^{\rm root,h}
 =\sum_{P:\,|P|=h}v_{U,\pi}^{\rm root}(P),
\tag{4.1}
\]

where the sum is over all \(M\) cyclic positional intervals of length
\(h\).  Define the direct deck analogously.

### Theorem 4.1 (optimal nonzero restitution)

For every \(2\le h\le2H\), the six-frame root-deck derivative satisfies

\[
 \|\Delta_h^{\rm root}\|_2^2=8h.
\tag{4.2}
\]

Every one of the six individual swaps has squared action \(4h\), so

\[
 \sum_{i=0}^5
 \|c_{U_i,-}^{\rm root,h}-c_{U_i,+}^{\rm root,h}\|_2^2=24h.
\tag{4.3}
\]

The same identities hold for the direct \((M-h)\)-decks.  For the full
decks at \(h=0,1\), the derivative is zero.

#### Proof

There are exactly \(h\) length-\(h\) intervals containing \(A\), and
exactly \(h\) containing \(B\).  None contains another placeholder.
By (3.2), each of these \(2h\) phases contributes a context lift of
\(\eta\), with squared norm four.  For \(h\ge2\), their \((h-1)\)-set
contexts in \(C\) are distinct.  Equality of an \(A\)-context and a
\(B\)-context would make two cyclic \(h\)-intervals differ only in their
two endpoint placeholders, forcing the cyclic placeholder distance to
be \(h\), contrary to the gap assumption.  Hence all \(2h\) lifts are
orthogonal, proving (4.2).

For one top, swapping the far positions \(A,B\) changes exactly \(2h\)
old root-form windows, and no changed old window is a new window.  The
symmetric difference therefore has size \(4h\).  Summing over six tops
proves (4.3).

Global complementation is an isometry and sends a root-form \(h\)-deck
to a direct \((M-h)\)-deck.  The full zero-, singleton-, and
co-singleton decks do not depend on the cyclic order, proving the final
claim. \(\square\)

## 5. Exact floor descent with a fixed closing collar

Let

\[
 P_h^+=\sum_{i=0}^5c_{U_i,+}^{\rm root,h},
 \qquad
 P_h^-=\sum_{i=0}^5c_{U_i,-}^{\rm root,h}.
\tag{5.1}
\]

Write

\[
 c_{t,\pm}^h=c_{V_t,\pm}^{\rm root,h},
 \qquad
 d_t^h=c_{t,-}^h-c_{t,+}^h.
\tag{5.2}
\]

Theorem 2.1 gives

\[
 P_h^--P_h^+=d_w^h-d_z^h.
\tag{5.3}
\]

### Lemma 5.1 (intrinsic flatness)

For every interval length and every common phase schedule,

\[
                         \|P^+\|_2=\|P^-\|_2.
\tag{5.4}
\]

#### Proof

The label involution

\[
 x_i\longmapsto x_{5-i}\quad(0\le i\le5)
\tag{5.5}
\]

fixes \(C,z,w\).  It reverses the five-edge \(z\)-path and the exceptional
\(w\)-edge, and maps the plus frame at each top to the minus frame at the
reflected top.  It does not move positional phases.  Thus it sends
\(P^+\) to \(P^-\), and coordinate relabelling preserves Euclidean norm.
\(\square\)

### Theorem 5.2 (simultaneous floor-corrected descent)

Keep the closing top \(V_z\) in its minus frame and put

\[
 L_{\rm old}=P_h^++c_{z,-}^h,
 \qquad
 L_{\rm new}=P_h^-+c_{z,-}^h.
\tag{5.6}
\]

For every integer \(c\) and every \(2\le h\le2H\),

\[
 \Phi_c(L_{\rm new})-\Phi_c(L_{\rm old})=-2h.
\tag{5.7}
\]

The direct \((M-h)\)-deck has the same descent.

#### Proof

The total coordinate sum of a deck is unchanged, so for any derivative
\(\delta\),

\[
 \Phi_c(L+\delta)-\Phi_c(L)
 =\langle L,\delta\rangle+\frac12\|\delta\|_2^2.
\tag{5.8}
\]

The baseline \(c\) disappears because \(\sum_T\delta_T=0\).

By Lemma 5.1, the intrinsic six-frame contribution to the difference is
zero.  It remains to evaluate the fixed collar against (5.3).  Every
target in the support of \(d_w^h\) omits \(w\): the changed short
root-form window contains \(A\) or \(B\), not the far placeholder \(D\).
Every target in \(c_{z,-}^h\) contains \(w\), because \(w\) belongs to
the root of \(V_z\).  Hence

\[
                         \langle c_{z,-}^h,d_w^h\rangle=0.
\tag{5.9}
\]

The two shores of the far transposition on \(V_z\) have equal norm and
symmetric difference \(4h\).  Therefore

\[
 \langle c_{z,-}^h,d_z^h\rangle
 =\langle c_{z,-}^h,c_{z,-}^h-c_{z,+}^h\rangle
 =2h.
\tag{5.10}
\]

Equations (5.3), (5.9), and (5.10) give a collar contribution \(-2h\).
The intrinsic contribution is zero, proving (5.7).  Complementation
proves the direct-deck statement. \(\square\)

If several signed depths are assigned nonnegative weights \(a_h\), the
same literal frame choice gives total change

\[
                         -2\sum_{h=2}^{2H}a_hh.
\tag{5.11}
\]

There is no asymptotic loss: every displayed descent is an exact integer.

### Proposition 5.3 (the descent is exactly a two-collision fan)

For every \(2\le h\le2H\), the seven decks in \(L_{\rm old}\) have
exactly \(2h\) unordered colliding target pairs and no target of
multiplicity at least three.  The seven decks in \(L_{\rm new}\) are
pairwise disjoint.  The same statement holds for the direct
\((M-h)\)-decks.

#### Proof

It is clearest to complement a root-form target.  The complement of a
root-form \(h\)-target from a top \(C\cup T\), where \(|T|=3\), is the
direct \((M-h)\)-interval

\[
 (C\setminus K)\cup(T\setminus S).
\tag{5.12}
\]

Because the placeholders are separated, \(S\) has size at most one.
Thus its external part has size two or three.

Two of the present tops can have a common target only if their external
triples share two labels.  They must then each omit their one noncommon
external label.  If those two noncommon labels occupy the same
placeholder position, the \(h\) intervals through that position give
exactly \(h\) common targets.  If they occupy different placeholder
positions, equality of their \((h-1)\)-element \(C\)-contexts would make
two cyclic \(h\)-intervals differ only in those two placeholder
positions.  Their cyclic distance would then be \(h\), contrary to the
gap hypothesis.  Hence there is no collision in the latter case.

Within the five-edge \(z\)-path, adjacent external triples share two
labels.  On the plus shore their two noncommon labels occupy \(A,B\),
respectively; on the minus shore they occupy \(B,A\).  Hence neither
shore has a path-internal collision.  Nonadjacent path triples share at
most \(z\), and the exceptional \(w\)-triple shares at most one label
with every path triple, so they cannot collide.

The fixed closing \(z\)-triple \(\{x_5,x_0,z\}\) shares two labels only
with the endpoint triples

\[
 \{x_0,x_1,z\},\qquad \{x_4,x_5,z\}.
\tag{5.13}
\]

On the old plus shore, its unique label and the closing triple's unique
label occupy \(B,B\) at the first endpoint and \(A,A\) at the second.
This gives \(h+h=2h\) common targets.  On the new minus shore the
corresponding positions are \(A,B\) and \(B,A\), so there is no common
target.  The two collision families have different external parts,
\(\{x_0,z\}\) and \(\{x_5,z\}\), and hence cannot form a triple
collision.  This proves the root-form statement.  Global
complementation proves the direct statement. \(\square\)

## 6. Sharp pair-boundary lower bound

Consider an arbitrary common-base bank of three-placeholder swaps.  Its
top indexed by \(e\) is

\[
 C\cup\{a_e,b_e,d_e\},
\tag{6.1}
\]

and the move swaps \(a_e,b_e\) between \(A,B\), keeping \(d_e\) at
\(D\).  Define the singleton and pair boundaries

\[
 \beta=\sum_e(e_{b_e}-e_{a_e}),
\qquad
 \xi=\sum_e
       (e_{\{b_e,d_e\}}-e_{\{a_e,d_e\}}).
\tag{6.2}
\]

### Theorem 6.1 (minimal higher-character action)

If \(\beta=0\) and \(\xi\ne0\), then

\[
 \partial_1\xi=0,
 \qquad
 \|\xi\|_2^2\ge4.
\tag{6.3}
\]

Under the separated-placeholder hypothesis, every full root-form
\(h\)-deck, \(2\le h\le2H\), consequently satisfies

\[
                         \|\Delta_h\|_2^2\ge8h.
\tag{6.4}
\]

The six-frame construction attains equality.

#### Proof

Taking the point boundary of one pair difference gives

\[
 \partial_1
 (e_{\{b_e,d_e\}}-e_{\{a_e,d_e\}})
 =e_{b_e}-e_{a_e}.
\tag{6.5}
\]

Thus \(\partial_1\xi=\beta=0\).  Also the sum of the coefficients of
\(\xi\) is zero.  A nonzero integral vector of squared norm below four
would have either one nonzero coefficient, two coefficients \(+1,-1\),
or three coefficients of magnitude one.  The first and third cases
contradict zero coefficient sum.  In the second case, zero point boundary
would force the two unordered pairs to have the same incidence vector,
and hence to be the same pair, making \(\xi=0\).  Therefore
\(\|\xi\|_2^2\ge4\).

The proof of Theorem 4.1 applies verbatim with \(\xi\) in place of
\(\eta\), giving

\[
                         \|\Delta_h\|_2^2
                         =2h\|\xi\|_2^2.
\tag{6.6}
\]

Equations (0.3) and (3.3) show equality for the displayed construction.
\(\square\)

## 7. Exact support factorization and the remaining boundary

The positive descent above must not be misreported as a new irreducible
six-top direction.  The phasewise identity (2.1) says precisely that its
load derivative is the difference of two one-top closing derivatives.
The pair rectangle (0.3) is already obtained from the two tops

\[
 C\cup\{x_5,x_0,z\},
 \qquad
 C\cup\{x_5,x_0,w\},
\tag{7.1}
\]

by orienting their swaps oppositely.  Thus two tops are enough in the
unrestricted load semigroup.

If the first top in (7.1) is protected and must not be changed, replace
its derivative by any common-\(z\) path from \(x_0\) to \(x_5\).  A
path with one new internal label has two edges.  Together with the
closing \(w\)-edge this uses three changed tops and has the same
phasewise derivative.  The cycle reflection and collar proof above work
unchanged.  Hence even the protected-closing version is not intrinsically
six-supported.

What six stages can supply is availability: they synthesize the forbidden
\(-d_z\) direction while leaving the actual \(V_z\) frame fixed.  To turn
that availability into a global theorem one still must prove that the old
and new shores can be embedded in the current owner-disjoint packing and
that a positive density of fixed collars has the favorable orientation.
Neither follows from the local identity.  This is the exact boundary of
the present result.
