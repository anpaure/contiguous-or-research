# Audit of three conformal-reserve candidates

**Date:** 2026-08-13  
**Method:** literal cyclic-window expansion, sign audit, and an adversarial
polynomial forbidden-bank test.  No computation or search was used.

## 1. Inputs and verdict

The audited attachments are:

1. `be63bec2-2f86-45cd-9c9b-aa76c3b517fa/pasted-text.txt`, SHA256
   `15aa7c0f0abf216d73c6ab66267349c9bd5968129ee930f290bf06b1110f09`;
2. `ffc98b05-8d10-4190-a3f1-0757cb60cf6b/pasted-text.txt`, SHA256
   `fa2839d609d6341b312795d7794ed83e7587ed09d516a20e4118c201df35aec1`;
3. `5ec15afb-4a96-4ec3-b3f1-a92cb96ee3e5/pasted-text.txt`, SHA256
   `37b04e2efa128da9ce6deae100bdf72de51f08453c3aaff9e1b73aaa2441fa7c`.

The proof-safe ranking is:

* **strongest positive result:** the short-period insertion-star theorem
  in the second attachment;
* **valid local result:** the adjacent-square four-rail lift in the first
  attachment, together with only a multiset-valued global consequence;
* **failed global claim:** the squarefree period-\(M\) reserve theorem in
  the third attachment.

## 2. PASS: short-period insertion-star packing

Put \(q=d+1\), \(c=R-q\), \(M=k-c\), and \(t=4q+4\).  Under

\[
 q\ge20,\qquad c\ge q+2,\qquad M-2\ge t,
\]

the construction in the second attachment is a genuine positive packing
of actual closed rail columns.

For an insertion of \(z\) into a period-\(t\) rail, write

\[
 F^+=G\mathbin{\dot\cup}P,\qquad
 F^-=G\mathbin{\dot\cup}N.
\]

Literal cyclic-window counting gives

\[
 |G|=t-q+1,qquad |P|=q,qquad |N|=q-1,
\]

and

\[
 \deg(P)-\deg(N)={\bf1}_D+q e_z.
\]

Coupling the \(q-1\) repeated centre insertions to their leaf insertions
with the same order and cut gives exactly the established star current

\[
 Y_H=\Delta_x+
 \sum_{p\in P\setminus\{x\}}(X_p-L_p),
 \qquad P_RY_H={\bf1}_H.
\]

Its boundary shores satisfy

\[
 Y_H^+=\{H\}\mathbin{\dot\cup}B_H^-,
 \qquad Y_H^-=B_H^+,
 \qquad |B_H^+|=|B_H^-|=2q(q-1).
\]

The random-order argument for the repeated centre core is valid.  For a
fixed width \(w\in\{q-1,q,q+1\}\), an old \(w\)-set occurs as a cyclic
window with probability \(t/\binom tw\), while a fixed augmented target
\(\{z\}\cup J\) occurs on the insertion boundary with probability
\(w/\binom t{w-1}\).  The displayed estimate in the attachment is below
one for every greedy stage when \(q\ge20\).  Hence all repeated-centre
owner and immediate-palette decks can be made disjoint.  Different leaf
cores are separated by their omitted leaf label; centre and leaf cores by
the label \(x\); and the insertion core from every star core by
\(2c>R+1\).  These are literal separation arguments, not generic
degree-fibre assertions.

Consequently there are two owner-disjoint closed-rail states

\[
 \operatorname{supp}{\cal Q}_H^0
   =R_H\mathbin{\dot\cup}B_H^+,
\]

\[
 \operatorname{supp}{\cal Q}_H^1
   =R_H\mathbin{\dot\cup}\{H\}
      \mathbin{\dot\cup}B_H^-,
\]

with \(2q-1\) rails in each state and

\[
 |R_H|=(2q-1)(t-q+1).
\]

Every rail has positive owner run \(q\), zero run at least \(3q+4\),
zero closed-trace boundary, and simple immediate lower and upper rows.
The unchanged insertion windows form a common literal path of length
\(t-q+1=3q+5\), so they provide geometric room for a private local
annotation.  This does not itself prove a typed suffix router.

### Exact scope correction

The state difference is

\[
 {\bf1}_{\operatorname{supp}{\cal Q}_H^1}
 -{\bf1}_{\operatorname{supp}{\cal Q}_H^0}
 =e_H+B_H^- -B_H^+=Y_H,
\]

not \(e_H\).  Thus this is an exact positive realization of the signed
macro \(Y_H\).  It becomes a one-owner absorber only in a background that
simultaneously exchanges \(B_H^+\) for \(B_H^-\).  The theorem does not
yet balance the full all-width/Ferrers ticket current or prove the global
common-cap cut.

## 3. PASS locally: adjacent-square four-rail lift

For an adjacent context square

\[
 K=A\cup\{a\},\qquad L=A\cup\{b\},
\]

choose an ordered \((q-1)\)-set \(J\subseteq A\) and put

\[
 D=K\setminus J,qquad D'=L\setminus J.
\]

The four period-\((M-1)\) rails in the first attachment give the exact
actual-column identity

\[
 f(Q_D^p)+f(Q_{D'}^x)-f(Q_D^x)-f(Q_{D'}^p)
 =e_{Kp}+e_{Lx}-e_{Kx}-e_{Lp}.
\]

The common reserve is literally

\[
 {cal R}=G_D\mathbin{\dot\cup}G_{D'}
 \mathbin{\dot\bigcup}_{s=1}^{q-1}
       \{M_s p,M_s x\},
 \qquad |{cal R}|=2M-4.
\]

Cross-core equality would force the unique non-special windows beginning
at \(b\) and \(a\) to agree.  Their final guards are chosen as distinct
labels \(w,w'\), so the two rails in either shore are owner-disjoint.
The remaining possible crossings contain different special labels and
are impossible.  Residence and trace claims follow componentwise: each
toggle run has length \(q\), each zero run has length \(M-1-q\), and each
rail is closed.

Telescoping along context paths therefore proves a nonnegative common-
reserve identity **with multiplicity** for the full special residual
\(B^+-B^-\).  It does not prove that reserves for distinct squares are
simultaneously squarefree.

There is also a genuine proper-width obstruction inside this four-rail
gadget: at each \(1\le h<q\), the two same-shore rails share the target

\[
 D\cup\{b,v_1,\ldots,v_{h-1}\}
 =D'\cup\{a,v_1,\ldots,v_{h-1}\}.
\]

Thus the local result is proof-safe exactly in the owner/trace/residence
projection; it is not an all-width simple absorber.

## 4. FAIL: the period-\(M\) squarefree reserve

The third attachment correctly derives the adjacent-transposition rail
identity and its pathwise telescoping as a **multiset identity**.  Its
Theorem 1 nevertheless asserts a simple owner reserve.  The first missing
step is Section 1.7's claim that polynomially many forbidden owners can be
avoided by the factorial freedom in the local order.

Fix the first context \(G\), a neighbour \(G'=D\mathbin{\dot\cup}F\),
and write

\[
 G=D\mathbin{\dot\cup}A,qquad |A|=q-1.
\]

The required local order contains the consecutive block

\[
 A,\ x,\ p,\ F.
\]

If \(u\) is the first element in the chosen order of \(A\), then the
common \(q\)-window ending at \(p\) is forced to be

\[
 W_u=D\cup(A\setminus\{u\})\cup\{x,p\}
     =(G\setminus\{u\})\cup\{x,p\}.
\]

For a fixed \(u\in A\), this owner appears with probability
\(1/(q-1)\), not a factorially small probability.  More decisively, the
polynomial forbidden family

\[
 {cal F}_G={
 (G\setminus\{u\})\cup\{x,p\}:u\in G
 \}
\]

has only \(R-1=O(k)\) members but intersects the common deck of **every**
possible first edge leaving \(G\), for every choice of its exact-distance
core \(D\) and every order of \(A\).  Choosing the context first and the
order second therefore does not repair the quantifier.

This does not prove that a specially coordinated global reserve is
impossible.  It proves that the stated greedy/union-bound argument does
not establish it.  Consequently equations (1.32)--(1.38) of that
attachment are valid algebraic common-reserve identities with
multiplicity, while its claimed owner-disjoint assembly, Theorem 1, and
all consequences depending on that squarefree assembly remain unproved.

## 5. Final proof boundary

The strongest new actual-column fact among the three candidates is:

> The explicit insertion-star macro \(Y_H\) has a squarefree positive
> two-state realization by \(2q-1\) short-period resident rails per state,
> with exact owner and immediate-palette simplicity.

The strongest independent local trade is:

> Every adjacent named-owner square has a literal resident four-rail
> common reserve, but it forces proper-width duplicates and composes only
> as a multiset without an additional squarefree theorem.

Neither statement is yet a full one-owner, all-width, common-cap absorber.
