# Independent audit: PBBS split-role-zero common-history holonomy

**Date:** 2026-08-13  
**Audited source:**
`MATH_OBSTRUCTION_PBBS_SPLIT_ROLEZERO_COMMON_HISTORY_HOLONOMY_20260813.md`  
**Audited source SHA-256:**
`5ccbdf2cb78504254b4d9dc0c1dbcc40e1ebcc70105451c7d2463db1fb6a13ef`  
**Verdict:** PASS for the exact scope stated in Theorem 3.1.

## 1. Core-difference identities

From

\[
 H_h=\{0\}\cup\{h+2,\ldots,2h\}
       \cup\{2h+4,2h+6,\ldots,2r\}
\]

one obtains literally

\[
 H_{h-1}\setminus H_h=\{h+1,2h+2\}=X_h,
 \qquad
 H_h\setminus H_{h-1}=\{2h-1,2h\}=Y_{h-1}.
\]

Consequently both displays of the shared owner are correct:

\[
 U_h=H_h\cup X_h=H_{h-1}\cup Y_{h-1}.
\]

## 2. Literal source overlap

An edge represented by the length-`d+2` source block

\[
 (W_h,C_{h,1},\ldots,C_{h,d},Y_h)
\]

and its consecutive successor edge have source blocks whose starting
positions differ by one.  Therefore the successor block must begin with

\[
 (C_{h,1},\ldots,C_{h,d},Y_h).
\]

Equating this with

\[
 (X_{h+1},C_{h+1,1},\ldots,C_{h+1,d},Z_{h+1})
\]

gives exactly

\[
 C_{h,1}=X_{h+1},\qquad
 C_{h+1,j}=C_{h,j+1}\ (j<d),\qquad
 C_{h+1,d}=Y_h.
\]

This is equality of ordered source letters, not merely equality of their
unions.  The recurrence is therefore necessary.

## 3. Index replay

Starting at the junction from height `h-1` to height `h`, the first `d`
junctions successively expose all entries of the old history and force

\[
 (C_{h-1,1},\ldots,C_{h-1,d})
   =(X_h,X_{h+1},\ldots,X_{h+d-1}).
\]

After these `d` shifts the first appended block, `Y_{h-1}`, has reached
the first history position.  The next, namely the `(d+1)`-st, junction
therefore forces

\[
 X_{h+d}=Y_{h-1}.
\]

But

\[
 \max X_{h+d}=2h+2d+2>2h=\max Y_{h-1}
\]

for every `d>=1`.  Thus the contradiction and the `d+1`-junction bound
are correctly indexed.  A direct replay at `d=1` gives the same first
failure after two junctions.

## 4. Scope

The proof rules out only the continuous all-height chain in which the two
halves at each height reuse one identical ordered partition.  It does not
rule out an isolated macro, at most `d` consecutive junctions, a genuine
history reset inside the detour, or auxiliary occurrence-transport rails.
Those exclusions are stated accurately in the source.

The only source edit made during this audit was typographical: two doubled
commas in the displayed sets in equation (3.3) were removed before the
SHA above was frozen.
