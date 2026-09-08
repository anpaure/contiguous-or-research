# Owner-map audit for capped MNW contexts

This note records exactly what the MNW recursion does to a flipping cycle
and what it does **not** imply about the boundary-transposition quotient.
It uses no assumption about the connectivity of that quotient.

Throughout, `~w` denotes reverse-complement (the MNW mirror), `bar(w)`
denotes bitwise complement without reversal, and `o(z)` is the unique Dyck
root whose MSW path contains the middle-level word `z`.

## 1. Exact recursive owner map

MNW equation (8) gives the following coordinate-free description of `o`.
Every middle-level word belongs to exactly one of the following three cases.

1. If

   \[
      z=1u0v,\qquad u,v\in\mathcal D,
   \]

   then `z` is itself a Dyck root and

   \[
      o(z)=z.                                           \tag{1.1}
   \]

2. If

   \[
      z=1a1v,\qquad \widetilde a\in\mathcal B,
      \quad v\in\mathcal D,
   \]

   then

   \[
      o(z)=1\,\widetilde{o(\widetilde a)}\,0v.          \tag{1.2}
   \]

3. If

   \[
      z=0\overline u1a,\qquad u\in\mathcal D,
      \quad a\in\mathcal B,
   \]

   then

   \[
      o(z)=1u0\,o(a).                                   \tag{1.3}
   \]

Here `B` is the union of the two middle levels in the appropriate even
dimension.  The decompositions in (1.1)--(1.3) are the unique ones in the
proof of MNW Lemma 5.

Indeed, the middle piece of `P(1u0v)` consists of the words

\[
        1\,\widetilde z\,1v,
        \qquad z\in P(\widetilde u),
\]

and its final piece consists of

\[
        0\overline u1z,\qquad z\in P(v).
\]

Equations (1.2) and (1.3) follow immediately.  This is the exact tool that
must be used whenever ownership after a context operation is asserted.

There is one useful functorial identity.  If `V` is Dyck, then

\[
             o(zV)=o(z)V.                               \tag{1.4}
\]

This follows from
`rho(xV)=rho(x) || (|x|+rho(V))`: the initial part of `P(o(z)V)` is the
copy `P(o(z))V`.  There is no analogous general left-concatenation identity.

For reference, (1.2) specializes to an exact formula for the difficult
prefix family.  Let `U` be a nonempty Dyck word.  The word
`10 bar(U) y` starts with `1` and has already gone below height zero after
the first bit of `bar(U)`, so it is in case (1.2).  Let

\[
             0\overline U y=a1v                         \tag{1.5}
\]

be its unique case-(1.2) cut, characterized by
`tilde(a) in B` and `v in D`.  Then

\[
       \boxed{
       o(10\overline U y)=1\,\widetilde{o(\widetilde a)}\,0v.}
                                                            \tag{1.6}
\]

This recursive formula retains a state-dependent cut.  Nevertheless, the
dependence can be eliminated by a separate path-embedding argument.  The
exact result, proved in `MSW_PREFIX_CONTEXT_FUNCTOR.md`, is

\[
 o(10\overline U y)=\mathsf H_U(o(10y)),
 \qquad
 \mathsf H_U(1bR)=11\theta_b(U)R.                       \tag{1.6a}
\]

This is a new prefix-context theorem; it is not plain left concatenation.

For the wrapped family put `w=101 tilde(y) 1`.  If `w` is Dyck then
`o(w)=w`; otherwise write its unique case-(1.2) decomposition as
`w=1a1v`.  Then

\[
       \boxed{o(101\widetilde y1)
        =1\,\widetilde{o(\widetilde a)}\,0v.}             \tag{1.7}
\]

Again the cut depends on `y`.  Formulae (1.6) and (1.7), rather than a
left-concatenation rule, are the exact owner identities in the two delicate
contexts.

## 2. What MNW Lemma 7 does to a witnessing cycle

Let `C=(y_1,...,y_{2l})` witness a flippable tuple `tau`.  The proof of MNW
Lemma 7 gives the following exact transformed cycles.

* Appending a Dyck word `V`:

  \[
       \tau\longmapsto\tau V,
       \qquad C\longmapsto CV=(y_1V,\ldots,y_{2l}V).
                                                            \tag{2.1}
  \]

* Prepending a Dyck word `U`:

  \[
       \tau\longmapsto U\tau,
       \qquad C\longmapsto \overline U C
          =(\overline U y_1,\ldots,\overline U y_{2l}).
                                                            \tag{2.2}
  \]

  The complement in (2.2) is essential: all coordinates of `U` have been
  flipped before the copy of the old factor path is reached.

* The odd mirrored operation:

  \[
       \tau\longmapsto1\widetilde\tau0,
       \qquad C\longmapsto
       (1\widetilde y_1 1,\ldots,1\widetilde y_{2l}1),
                                                            \tag{2.3}
  \]

  up to reversal of the cyclic order.

After a left cap `10` is inserted, the owner roots that must be understood
are therefore

\[
\begin{array}{c|c}
\text{operation}&\text{owners after the cap swap}\\ \hline
\text{append }V&o(10y_iV),\\
\text{prepend }U&o(10\overline U y_i),\\
\text{mirror-wrap}&o(101\widetilde y_i1).
\end{array}                                               \tag{2.4}
\]

For appending, (1.4) yields the exact identity

\[
              o(10y_iV)=o(10y_i)V.                        \tag{2.5}
\]

Thus every capped owner-incidence certificate really does append a Dyck
suffix unchanged.

The other two rows of (2.4) do not follow from MNW Lemma 7.  If a factor
edge has endpoints `10a,10b`, prepending `U` via Lemma 7 only says that

\[
       \overline U10a\quad\hbox{and}\quad\overline U10b
                                                            \tag{2.6}
\]

belong to one transformed factor path.  The capped construction instead
needs information about

\[
       10\overline U a\quad\hbox{and}\quad10\overline U b.
                                                            \tag{2.7}
\]

The blocks `10` and `bar(U)` have changed order.  Concatenation of flip
sequences does not commute them.

Likewise, wrapping the edge `10a--10b` via Lemma 7 produces the factor edge

\[
  1\widetilde{(10a)}1--1\widetilde{(10b)}1
  =1\widetilde a101--1\widetilde b101,                    \tag{2.8}
\]

whereas the capped wrapped tuple requires ownership of

\[
              101\widetilde a1,\qquad101\widetilde b1.    \tag{2.9}
\]

Again, (2.8) and (2.9) have the cap in different positions.

## 3. A concrete obstruction already in the base pattern beta

The claim that every intervening edge of the displayed MNW cycle becomes
one MSW factor edge after capping is false already for `beta`.

The MNW cycle is

\[
 (111000,111001,011001,011011,011010,111010).
                                                            \tag{3.1}
\]

Its factor edges are the first-second, third-fourth, and fifth-sixth pairs.
Consequently, the closing edge

\[
                   111010--111000                           \tag{3.2}
\]

is an intervening edge.  After prefixing `10`, its endpoints are

\[
                   10111010,\qquad10111000.                \tag{3.3}
\]

The second word in (3.3) is Dyck, so

\[
                   o(10111000)=10111000.                    \tag{3.4}
\]

For the first word, use the case-(1.2) decomposition

\[
       10111010=1\,(01)\,1\,(1010).
\]

Since `o(01)=10` and both `10` and `1010` are Dyck,

\[
                   o(10111010)=11001010.                    \tag{3.5}
\]

The owners in (3.4) and (3.5) are different.  Thus (3.2) does not become
a single owner-path edge after capping.

The capped support of `beta` is nevertheless connected: it is connected
by other boundary witnesses (in fact by a star).  That is a different
certificate.  It cannot be obtained merely by walking around (3.1) and
declaring every intervening pair to have one owner.

The mirror-wrap shows the same non-functoriality even more sharply.  For
the closing pair in (3.1), the capped wrapped states include

\[
       1011010001,qquad1011110001.
\]

Repeated use of (1.2) gives

\[
\begin{aligned}
 1011010001&=1(01101000)1,
   &\widetilde{01101000}&=11101001,\\
 11101001&=1(110100)1,
   &o(11101001)&=1\widetilde{110100}0=11101000,\\
 o(1011010001)&=1\widetilde{11101000}0=1111010000;
\end{aligned}                                             \tag{3.6}
\]

where `110100` is Dyck.  Similarly,

\[
\begin{aligned}
 1011110001&=1(01111000)1,
   &\widetilde{01111000}&=11100001,\\
 11100001&=1(110000)1,
   &\widetilde{110000}&=111100,\\
 o(11100001)&=1\widetilde{111100}0=11100000,\\
 o(1011110001)&=1\widetilde{11100000}0=1111110000.
\end{aligned}                                             \tag{3.7}
\]

The final owners in (3.6) and (3.7) are different.  The known two-star connection for the
wrapped `beta` support uses additional vertices of the relevant MSW paths;
it is not the mirrored image of the capped walk asserted above.

## 4. Correct status of context preservation

The exact conclusions are:

1. Dyck-suffix appending preserves any capped owner certificate, by (2.5).
2. Dyck-prefix prepending is **not** justified by concatenation.  Its exact
   owner problem is the new family `o(10 bar(U) y)` in (2.4).
3. Mirror-wrapping is **not** an identical reversed capped walk.  The cap
   moves from (2.8) to (2.9), and (3.6)--(3.7) give an explicit failure of the
   purported owner equality.
4. The examples do not disprove that the capped support remains connected:
   `beta` and wrapped `beta` do remain connected through alternative stars.
   They disprove the proposed proof mechanism.  A general theorem asserting
   preservation of capped connectivity under the first and third operations
   would be a new lemma, not a consequence of MNW Lemma 7.

Accordingly, the MNW spanning-hypergraph argument for boundary connectivity
cannot be declared complete until explicit boundary witnesses are supplied
for arbitrary even-prefix and mirrored contexts, or boundary connectivity is
proved by a different recursion.

## 5. A clean replacement target

There is an exact neighbor formula that avoids all reference to flipping
cycles.  Since

\[
        \rho(10x)=(2,1,2+\rho(x)),
\]

the path `P(10x)` consists of

\[
        10x,\quad 11x,\quad 01z\quad(z\in P(x)),          \tag{5.1}
\]

with the last family in path order (and the common endpoint written only
once).  Swapping the first two coordinates in `01z` gives `10z`.  Therefore
the nontrivial boundary-neighbor set of a capped root has the exact form

\[
       \boxed{
       N_{\Gamma^{\partial}_{m+1}}(10x)
          =\{,o(10z):z\in P_m(x),\},}                   \tag{5.2}
\]

up to deletion of the root itself when graph loops are suppressed.

Thus the unresolved cap-connectivity statement is equivalently the
connectivity of the incidence graph whose left vertices are `10x`, whose
right vertices are the owner roots `o(10z)`, and whose incidences are
`z in P(x)`.  Formula (5.2), together with the recursive rules
(1.1)--(1.3), is a more promising rigorous starting point than trying to
transport MNW witness cycles through contexts: it asks for a spanning
connected owner-incidence scaffold and does not require any false
commutation of the cap with a context block.
